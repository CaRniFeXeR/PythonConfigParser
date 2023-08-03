from pathlib import Path
import unittest
from src.cfgparser.io.jsonfileloader import JsonFileLoader

from src.cfgparser.json_config_parser import JSONConfigParser





class IOTests(unittest.TestCase):


    # None given
    def test__load_jsonfile__empty_string_given__raise_exception(self):
        
        with self.assertRaises(Exception) as context:
            filereader = JsonFileLoader(None)

        exception_msg = str(context.exception)
        self.assertTrue("inputfile is empty" in exception_msg)

    # empty string given
    def test__load_jsonfile__empty_string_given__raise_exception(self):
        
        with self.assertRaises(Exception) as context:
            filereader = JsonFileLoader("")

        exception_msg = str(context.exception)
        self.assertTrue("inputfile is empty" in exception_msg)

    # file not found
    def test__load_jsonfile__non_existing_file_given__raise_exception(self):
        
        with self.assertRaises(Exception) as context:
            filereader = JsonFileLoader("non_existing_file.json")

        exception_msg = str(context.exception)
        self.assertTrue("'non_existing_file.json' does not exist" in exception_msg)

    # not a json
    def test__load_jsonfile__not_a_json_file_given__raise_exception(self):
        
        filereader = JsonFileLoader("src/test/json_cfgs/not_a_json.json")

        with self.assertRaises(Exception) as context:
            json_dict = filereader.loadJsonFile()

        exception_msg = str(context.exception)
        self.assertTrue("could not parse json file 'src" in exception_msg)



if __name__ == '__main__':
    unittest.main()