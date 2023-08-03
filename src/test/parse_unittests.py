from pathlib import Path
import unittest

from src.cfgparser.json_config_parser import JSONConfigParser





class ConfigParserTest(unittest.TestCase):

    def test__config_parser__complex_typed_list_given__types_correctly_parsed(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path(".\\src\\test\\json_cfgs\\complex_typed_list.json"))

        self.assertTrue(type(parsed_dummy_config).__name__ == "DummyConfig")

        for el in parsed_dummy_config.dummy_element_list:
            self.assertTrue(type(el).__name__ == "DummyConfigElement")

    def test__config_parser__missing_field__throws_correct_exception(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path(".\\src\\test\\json_cfgs\\missing_field.json"))

        exception_msg = str(context.exception)
        self.assertTrue("missing" in exception_msg)
        self.assertTrue("required positional argument" in exception_msg)
        self.assertTrue("another_list" in exception_msg)

    def test__config_parser__unkown_field__throws_correct_exception(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path(".\\src\\test\\json_cfgs\\unkown_field.json"))

        exception_msg = str(context.exception)
        self.assertTrue("unkown field name 'field_that_does_not_exist' for type" in exception_msg)

    def test__config_parser__missing_type_name__throws_correct_exception(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file(Path(".\\src\\test\\json_cfgs\\missing_type_name.json"))

        exception_msg = str(context.exception)
        self.assertTrue("'type_name' must be specified" in exception_msg)

    def test__config_parser__wrong_simple_type__throws_exception(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file(Path(".\\src\\test\\json_cfgs\\wrong_simple_type.json"))

        self.assertTrue(type(parsed_dummy_config.name).__name__ == "str")

    def test__parse_from_file__with_path_and_with_str__should_be_equal(self):
        
        parser = JSONConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config_path = parser.parse_from_file(Path(".\\src\\test\\json_cfgs\\complex_typed_list.json"))
        parsed_dummy_config_str = parser.parse_from_file(".\\src\\test\\json_cfgs\\complex_typed_list.json")

        self.assertEqual(parsed_dummy_config_path, parsed_dummy_config_str)


if __name__ == '__main__':
    unittest.main()
