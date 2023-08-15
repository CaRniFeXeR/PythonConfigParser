# PythonConfigParser


truly fully-typed python configs - not more, not less.
    
[![PyPI version](https://badge.fury.io/py/cfgparser.svg)](https://badge.fury.io/py/cfgparser)
![Badge Name](https://github.com/CaRniFeXeR/PythonConfigParser/actions/workflows/unittests.yml/badge.svg?branch=main&event=push)
[![codecov](https://codecov.io/gh/CaRniFeXeR/PythonConfigParser/main/graph/badge.svg)](https://codecov.io/gh/CaRniFeXeR/PythonConfigParser)


## Usage

1. define your config structure in a dataclass like

```python
from dataclasses import dataclass
from typing import List

@dataclass
class DummyConfigElement:
    name: str
    list: List[int]
    another_list: List[float]

```

2. initialize the config parser with the path to the module with the config definitions.


```python

parser = ConfigParser(datastructure_module_name="mysrc.datastructures.configs")
```

3. parse a config from file or dict

#### from file 



```python

my_config = parser.parse_from_file("myconfig.json")

```

#### from dictionary

```python

my_config_dict = {"type_name" : "mysrc.datastructures.configs.a", "value" : 1}
my_config = parser.parse(my_config_dict)

```


### Type definition
There are two ways to define the configs type:
- specified in the config itself
    - store fully qualified name of the config class under the key "type_name" in the config
    - e.g in the code example above
- specified when parsing the config
    - if the config has no key "typed_config" set, the type can be specified when parsing the config
    
```python
from mysrc.datastructures.configs import a
my_config_dict = {"some_key" : "some_value"}
# config has no key "type_name" but type is specified when parsing
my_config = ConfigParser().parse_typed(my_config_dict,a)

```

### Optional & Union fields
By default every field can be explicitly set to None. If you don't what this behavior you can set the flag "allow_none" to False.

```python
    from cfgparser import settings
    settings.allow_none = False
```

#### Union fields

Whenever a Union type is encountered the parser tries to parse the config with the first type in the union. If this fails it tries the next type and so on. If all types fail the parser raises an exception. For instance, in the example below the parser tries to parse the config as a Bird. If this fails it tries to parse it as a Cat. If this fails too the parser raises an exception.

```python

from dataclasses import dataclass
from typing import Union

@dataclass
class Bird:
    name: str
    wingspan: float

@dataclass
class Cat:
    name: str
    paws: int

@dataclass
class AnimalOwnership:
    owner: str
    animal : Union[Bird, Cat]

```

## Features

- ✅ fully typed json and yaml configs
- ✅ nested configs
- ✅ complex union and optional types
- ✅ dict object into typed dataclass
- ✅ support for enums (value given as string or int)
- ✅ support for typed tuples (e.g. Tuple[int, str, float])
- ✅ override type_name if type is specified when parsing



## Installation

```bash
pip install cfgparser
```

## Feature Roadmap

- ⬜ specify config from cli
- ⬜ post hock
- ⬜ distributed configs
- ⬜ typed dicts (e.g. Dict[str, MyType])
- ⬜ typed functions (e.g. torch.functional.relu)
- ⬜ save config to file (json, yaml) with and without typeinfo
