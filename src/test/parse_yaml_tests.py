from pathlib import Path
import unittest

from src.cfgparser.config_parser import ConfigParser





class YamlConfigParserTest(unittest.TestCase):

    def test__config_parser__complex_typed_list_given__types_correctly_parsed(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path("src/test/yaml_cfgs/complex_typed_list.yml"))

        self.assertTrue(type(parsed_dummy_config).__name__ == "DummyConfig")

        for el in parsed_dummy_config.dummy_element_list:
            self.assertTrue(type(el).__name__ == "DummyConfigElement")

    def test__config_parser__missing_field__throws_correct_exception(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path("src/test/yaml_cfgs/missing_field.yml"))

        exception_msg = str(context.exception)
        self.assertTrue("missing" in exception_msg)
        self.assertTrue("required positional argument" in exception_msg)
        self.assertTrue("another_list" in exception_msg)

if __name__ == '__main__':
    unittest.main()
