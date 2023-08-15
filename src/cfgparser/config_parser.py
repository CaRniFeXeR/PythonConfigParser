from typing import Tuple, Type
import typing
from .io.yamlfileloader import YamlFileLoader

from .utils.union_handler import is_union_type
from . import settings
from .io.jsonfileloader import JsonFileLoader
from pathlib import Path
from enum import Enum
import inspect



from .utils.dynamic_type_loader import load_type_dynamically_from_fqn

class ConfigParser:
    """
    Handles parsing of json and yaml config into typed dataclass
    """

    def __init__(self, datastructure_module_name: str = "src.datastructures") -> None:
        self.datastructure_module_name = datastructure_module_name

    def _load_config_file(self, config_path: Path) -> dict:
        if isinstance(config_path, str):
            config_path = Path(config_path)
        elif not isinstance(config_path, Path):
            raise TypeError("'config_path' must be a str or Path")

        if not config_path.exists():
            raise ValueError(f"given config_path '{config_path}' does not exist")

        if config_path.name.endswith(".json"):
            fileloader = JsonFileLoader(config_path)
        elif config_path.name.endswith(".yml") or config_path.name.endswith(".yaml"):
            fileloader = YamlFileLoader(config_path)
        else:
            raise ValueError(f"either .json or .yml or .yaml files expected but '{config_path.name}' given")
        
        config_dict = fileloader.load_file()

        return config_dict

    def parse_from_file(self, config_path: Path):
        """
        loads a json or yaml config from the specified location and parses it into a typed object based on the type specified in 'type_name'
        """

        config_dict = self._load_config_file(config_path)

        return self.parse(config_dict)
    
    def parse_form_file_typed(self, config_path: Path, target_type : Type):
        """
        loads a json or yaml config from the specified location and parses it into the given type
        """

        config_dict = self._load_config_file(config_path)

        return self.parse_typed(config_dict, target_type)

    def parse(self, config_dict: dict):
        """
        parse a config dict into a typed object based in on the type specified in 'type_name'
        """

        if not isinstance(config_dict, dict):
            raise TypeError("'config_dict' must be a dict")

        if "type_name" not in config_dict.keys():
            raise ValueError("'type_name' must be specified")

        target_type = load_type_dynamically_from_fqn(config_dict["type_name"])
        del config_dict["type_name"]  # should not be parsed

        return self.parse_typed(config_dict, target_type)

    def parse_typed(self, config_dict: dict, target_type: Type):
        """
        recursively converts a dict into the given dataclass type
        """

        if not isinstance(config_dict, dict) or not hasattr(target_type, "__dataclass_fields__"):
            return config_dict
        
        if "type_name" in config_dict.keys():
            # ignore type_name if it is in the dict
            config_dict.pop("type_name")

        result_dict = {}
        current_fields = target_type.__dataclass_fields__

        for k, v in config_dict.items():

            if k not in current_fields:
                raise TypeError(f"unkown field name '{k}' for type '{target_type.__name__}'")

            field = current_fields[k]
            result_dict[k] = self._parse_value(k, v, field.type)

        return target_type(**result_dict)

    def _parse_value(self, k : str, v, type : Type):
        if v is None and settings.allow_none:
            return None

        elif inspect.isclass(type) and issubclass(type, Enum):  # is Enum
            try:
                if isinstance(v, str):
                    return type[v]
                elif isinstance(v, int):
                    return type(v)
                else:
                    raise ValueError(f"value '{v}' must either be a str or int for enum of type '{type}'")
            except Exception as ex:
                raise ValueError(f"value '{v}' is not valid for enum of type '{type}' ") from ex

        elif type.__module__.startswith(self.datastructure_module_name):  # complex type from the specificed module
            return self.parse_typed(v, type)
        elif hasattr(type, "_name") and type._name == "List":

            if not isinstance(v, list):
                raise TypeError(f"'{k}' must be a list.")

            list_element_type = type.__args__[0]

            parsed_list = []
            for el in v:
                parsed_list.append(self.parse_typed(el, list_element_type))

            return parsed_list
            
        elif hasattr(type, "_name") and type._name == "Dict":
            return dict(v)
        elif is_union_type(type):
            return self._try_parse_union(k,v,type)
        elif typing.get_origin(type) is tuple:
            return self._try_parse_tuple(k,v,type)
        else:
            # normal standard type that can be initated with its value
            return type(v)

    def _try_parse_union(self, k : str, value, union_type : Type):
        """
        try to parse given value to the given union type,
        first sucessful parse will be returned
        """
        unioned_types = typing.get_args(union_type)

        for unioned_type in unioned_types:
            if unioned_type == type(None):
                if value == None:
                    return None
            else:
                try:
                    return self._parse_value(k,value, unioned_type)
                except:
                    pass

        raise TypeError(f"could not parse value '{value}' to any of the unioned types {unioned_types}")
    
    def _try_parse_tuple(self, k : str, value, tuple_type : Type):
        """
        try to parse given value to the given tuple type
        """
        
        if not hasattr(value, '__len__'):
            raise TypeError(f"could not parse value '{value}' to tuple type {tuple_type}. Value needs to be length-able.")
        
        tuple_types = typing.get_args(tuple_type)

        #check if number of elements in tuple is correct
        if len(value) != len(tuple_types):
            raise TypeError(f"tuple '{k}' must have exactly {len(tuple_types)} elements")
        try:        

            tuple_values = []

            for tuple_type, tuple_value in zip(tuple_types, value):
                #parse each element of the tuple
                tuple_values.append(self._parse_value(k,tuple_value, tuple_type))

            return tuple(tuple_values)

        except Exception as ex:
            raise TypeError(f"could not parse value '{value}' to tuple type {tuple_type}") from ex