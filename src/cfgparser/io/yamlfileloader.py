from .fileloader import FileLoader
import yaml


class YamlFileLoader(FileLoader):
    """
    Handles YAML File loading
    """

    def load_file(self):
        return self.loadYamlFile()

    def loadYamlFile(self) -> dict:
        with open(self.inputfile) as yaml_file:
            try:
                config_dict = yaml.safe_load(yaml_file)
            except Exception as e:
                raise ValueError(f"could not parse yaml file '{self.inputfile}'") from e

        return config_dict
