from pathlib import Path
from typing import List
import unittest
from dataclasses import dataclass

from src.cfgparser.json_config_parser import JSONConfigParser



@dataclass
class DummyConfigElement:
    name: str
    list: List[int]
    another_list: List[float]


@dataclass
class DummyConfig:
    config_name: str
    dummy_element: DummyConfigElement
    dummy_element_list: List[DummyConfigElement]
    second_dummy_element: DummyConfigElement = DummyConfigElement("dummy_config el", [1], [0.4, 0.5])


class ConfigParserTest(unittest.TestCase):

    def test_config_parser_complex_typed_list(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.parse_unittests")

        parsed_dummy_config = parser.parse_config_from_file(Path(".\\src\\test\\test_configs\\complex_typed_list.json"))

        self.assertTrue(type(parsed_dummy_config).__name__ == "DummyConfig")

        for el in parsed_dummy_config.dummy_element_list:
            self.assertTrue(type(el).__name__ == "DummyConfigElement")

    def test_config_parser_missing_field(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.parse_unittests")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_config_from_file(Path(".\\src\\test\\test_configs\\missing_field.json"))

        exception_msg = str(context.exception)
        self.assertTrue("missing" in exception_msg)
        self.assertTrue("required positional argument" in exception_msg)
        self.assertTrue("another_list" in exception_msg)

    def test_config_parser_unkown_field(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.parse_unittests")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_config_from_file(Path(".\\src\\test\\test_configs\\unkown_field.json"))

        exception_msg = str(context.exception)
        self.assertTrue("unkown field name 'field_that_does_not_exist' for type" in exception_msg)

    def test_config_parser_missing_type_name(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.parse_unittests")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_config_from_file(Path(".\\src\\test\\test_configs\\missing_type_name.json"))

        exception_msg = str(context.exception)
        self.assertTrue("'type_name' must be specified" in exception_msg)

    def test_config_parser_wrong_simple_Type(self):

        parser = JSONConfigParser(datastructure_module_name="src.test.parse_unittests")

        parsed_dummy_config = parser.parse_config_from_file(Path(".\\src\\test\\test_configs\\wrong_simple_type.json"))

        self.assertTrue(type(parsed_dummy_config.name).__name__ == "str")


if __name__ == '__main__':
    unittest.main()
