from pathlib import Path
import unittest

from src.cfgparser.config_parser import ConfigParser
from src.cfgparser.utils.dynamic_type_loader import load_type_dynamically_from_fqn





class TypeLoadingTests(unittest.TestCase):

    def test__config_parser__complex_typed_list_given__types_correctly_parsed(self):
        with self.assertRaises(Exception) as context:
            load_type_dynamically_from_fqn("no.a.type")

        exp_msg = str(context.exception)
        self.assertTrue("exception while dynamically loading type:" in exp_msg)

if __name__ == '__main__':
    unittest.main()
