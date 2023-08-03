# PythonConfigParser

Typed Python JSON configparser based on Python dataclasses.

## Usage

define your config stucture in a dataclass like

```python
from dataclasses import dataclass
from typing import List

@dataclass
class DummyConfigElement:
    name: str
    list: List[int]
    another_list: List[float]

```

### from file 

First initialize the config parser with the path to the module with the config definitions.

```python

parser = JSONConfigParser(datastructure_module_name="mysrc.datastructures.configs")
# Then parse the config from file.
my_config = parser.parse_config_from_file("myconfig.json")

```

### from dictionary

```python

my_config_dict = {"type_name" : "mysrc.datastructures.configs.a"}
my_config = JSONConfigParser().parse_config(my_config_dict)

```


#### type definition
There are two ways to define the configs type:
- specified in the config itself
    - e.g in the code example above
    - path to the config class must be specified as str in the config as key "type_name"
- specified when parsing the config
    - if the config has no key "typed_config" set, the type can be specified when parsing the config
    
```python
from mysrc.datastructures.configs import a
my_config_dict = {"some_key" : "some_value"}
my_config = JSONConfigParser().parse_config_into_typed_object(my_config_dict,a)

```



## Features

- fully typed json configs
- nested configs
- dict object into typed dataclass

## Installation

```
pip install cfgparser
```

## Comming Features

- yaml support
- typed optional support
- specify config from cli
