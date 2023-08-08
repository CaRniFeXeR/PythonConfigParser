from pathlib import Path
import unittest

from src.cfgparser.config_parser import ConfigParser





class ParserTest(unittest.TestCase):

    def test__config_parser__complex_typed_list_given__types_correctly_parsed(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(343)

        exception_msg = str(context.exception)
        self.assertTrue("'config_path' must be a str or Path" in exception_msg)

    # wrong extension
    def  test__load_file__wrong_file_extension__raise_exception(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config_path = parser.parse_from_file(Path("src/test/wrong_extention.wrong"))

        exception_msg = str(context.exception)
        self.assertTrue("either .json or .yml or .yaml files expected but" in exception_msg)

    #non exiting path
    def test__load_file__path_not_existing__raise_exception(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config_path = parser.parse_from_file(Path("src/test/non_existing_path.json"))

        exception_msg = str(context.exception)
        self.assertTrue("given config_path" in exception_msg)
        self.assertTrue("does not exist" in exception_msg)

    def test__parse_dict__no_dict_given__raise_exception(self):
        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")
            
        with self.assertRaises(Exception) as context:
            parsed_dummy_config_path = parser.parse(343)

        exception_msg = str(context.exception)
        self.assertTrue("'config_dict' must be a dict" in exception_msg)


if __name__ == '__main__':
    unittest.main()
