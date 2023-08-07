import yaml

def yaml_to_dict(yaml_data):
    try:
        parsed_dict = yaml.safe_load(yaml_data)
        return parsed_dict
    except yaml.YAMLError as e:
        print("Error while parsing YAML data:", e)
        return None

# Example usage
yaml_data = """
key1: value1
key2:
  - item1
  - item2
key3:
  subkey1: subvalue1
"""

parsed_dict = yaml_to_dict(yaml_data)
print(parsed_dict)
