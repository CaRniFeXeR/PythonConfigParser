from .fileloader import FileLoader
import json


class JsonFileLoader(FileLoader):
    """
    Handles JSON File loading
    """

    def loadJsonFile(self) -> dict:
        with open(self.inputfile) as json_file:
            try:
                config_dict = json.load(json_file)
            except Exception as e:
                raise ValueError(f"could not parse json file '{self.inputfile}'") from e

        return config_dict
