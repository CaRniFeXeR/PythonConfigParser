from pathlib import Path
import unittest

from src.cfgparser.config_parser import ConfigParser
from src.test.datastructure.dummy_cfgs import DummyEnum, DummyEnumConfig





class ParseEnumTests(unittest.TestCase):

    def test__config_praser__given_enum_str__parse_enum_correctly(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file_typed(Path("src/test/yaml_cfgs/enum_str_config.yml"), DummyEnumConfig)

        self.assertTrue(isinstance(parsed_dummy_config, DummyEnumConfig))
        self.assertTrue(parsed_dummy_config.enum, DummyEnum.RED)

    def test__config_praser__given_enum_int__parse_enum_correctly(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        parsed_dummy_config = parser.parse_from_file_typed(Path("src/test/yaml_cfgs/enum_int_config.yml"), DummyEnumConfig)

        self.assertTrue(isinstance(parsed_dummy_config, DummyEnumConfig))
        self.assertTrue(parsed_dummy_config.enum, DummyEnum.ORANGE)

    def test__config_praser__given_enum_float__thows_exception(self):

        parser = ConfigParser(datastructure_module_name="src.test.datastructure.dummy_cfgs")

        with self.assertRaises(Exception) as context:
            parsed_dummy_config = parser.parse_from_file_typed(Path("src/test/yaml_cfgs/enum_float_config.yml"), DummyEnumConfig)

        exp_msg = str(context.exception)
        self.assertTrue("not valid for enum" in exp_msg)
        # self.assertTrue("must either be a str or int" in exp_msg)