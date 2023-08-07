from pathlib import Path
import unittest
from src.cfgparser.io.jsonfileloader import JsonFileLoader

from src.cfgparser.json_config_parser import JSONConfigParser
from src.test.datastructure.dummy_cfgs import DummyConfigElement
import src.cfgparser as cfgparser




class AdvancedTypesTests(unittest.TestCase):

    # Optional set
    def test__parse__optional_set__parse_correctly(self):
        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/correct_optional.json"))

        self.assertTrue(len(parsed_dummy_config.optional_list) > 0)
        self.assertTrue(parsed_dummy_config.optional_el is not None)
        self.assertTrue(isinstance(parsed_dummy_config.optional_el,DummyConfigElement))
        self.assertTrue(isinstance(parsed_dummy_config.optional_list[0],float))

    # Optional not set
    def test__parse__optional_not_set__no_error(self):
        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/optional_not_set.json"))

        self.assertTrue(parsed_dummy_config.optional_list is None)
        self.assertTrue(parsed_dummy_config.optional_el is None)
    
    # Optional set to wrong type
    def test__parse__optional_set_to_wrong_type__raise_error(self):
        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

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
        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/json_cfgs/none_fields.json"))

        exception_msg = str(context.exception)
        self.assertTrue("must be a list" in exception_msg)



if __name__ == '__main__':
    unittest.main()