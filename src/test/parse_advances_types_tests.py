from pathlib import Path
import unittest

from src.cfgparser.config_parser import ConfigParser
from src.test.datastructure.dummy_cfgs import DummyConfigElement
from src import cfgparser




class AdvancedTypesTests(unittest.TestCase):

    # Optional set
    def test__parse__optional_set__parse_correctly(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/correct_optional.json"))

        self.assertTrue(len(parsed_dummy_config.optional_list) > 0)
        self.assertTrue(parsed_dummy_config.optional_el is not None)
        self.assertTrue(isinstance(parsed_dummy_config.optional_el,DummyConfigElement))
        self.assertTrue(isinstance(parsed_dummy_config.optional_list[0],float))

    # Optional not set
    def test__parse__optional_not_set__no_error(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/optional_not_set.json"))

        self.assertTrue(parsed_dummy_config.optional_list is None)
        self.assertTrue(parsed_dummy_config.optional_el is None)
    
    # Optional set to wrong type
    def test__parse__optional_set_to_wrong_type__raise_error(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/optional_set_to_wrong_type.json"))

        exception_msg = str(context.exception)
        self.assertTrue("could not parse value" in exception_msg)
        self.assertTrue("List[float]" in exception_msg)


    # nested optional not set
    #TODO

    #strict none mode on
    def test__parse_without_none_allowed__none_given__raise_error(self):
        cfgparser.settings.allow_none = False
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/none_fields.json"))

        exception_msg = str(context.exception)
        self.assertTrue("must be a list" in exception_msg)

    def test__parse_without_none_allowed_none_given_in_optional__no_error(self):
        cfgparser.settings.allow_none = False
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")
        parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/optional_set_to_none.json"))

    #region [Tuple]
    def test__parse_typed_tuple__tuple_given_with_complex_types_given__parse_correctly(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")
        parsed_dummy_config = parser.parse_from_file(Path("src/test/yaml_cfgs/tuple.yml"))

        self.assertTrue(isinstance(parsed_dummy_config.min_max,tuple))
        self.assertTrue(isinstance(parsed_dummy_config.from_to_time,tuple))
        self.assertTrue(isinstance(parsed_dummy_config.from_to_time[0],int))
        self.assertTrue(isinstance(parsed_dummy_config.from_to_time[1],str))
        self.assertTrue(isinstance(parsed_dummy_config.from_to_time[2],int))
        self.assertTrue(isinstance(parsed_dummy_config.from_to_time[3],str))

    def test__parse_typed_tuple__to_enough_values_given__raise_excpetion(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/yaml_cfgs/tuple_to_few_values.yml"))

        exception_msg = str(context.exception)
        self.assertTrue("must have exactly 4 element" in exception_msg)

    def test__parse_typed_tuple__just_a_number_given__raise_non_lengthable_exception(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/yaml_cfgs/tuple_just_a_number.yml"))

        exception_msg = str(context.exception)
        self.assertTrue("Value needs to be length-able." in exception_msg)

    def test__parse_typed_tuple__one_value_with_wrong_type__raise_exception(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/yaml_cfgs/tuple_one_value_with_wrong_type.yml"))

        exception_msg = str(context.exception)
        self.assertTrue("could not parse value" in exception_msg)

    #endregion

if __name__ == '__main__':
    unittest.main()