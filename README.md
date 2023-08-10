# PythonConfigParser


easy, light-weight fully-typed python configs.
not more, not less.
    
[![PyPI version](https://badge.fury.io/py/cfgparser.svg)](https://badge.fury.io/py/cfgparser)
![Badge Name](https://github.com/CaRniFeXeR/PythonConfigParser/actions/workflows/unittests.yml/badge.svg?branch=main&event=push)
[![codecov](https://codecov.io/gh/CaRniFeXeR/PythonConfigParser/main/graph/badge.svg)](https://codecov.io/gh/CaRniFeXeR/PythonConfigParser)


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

parser = ConfigParser(datastructure_module_name="mysrc.datastructures.configs")
# Then parse the config from file.
my_config = parser.parse_from_file("myconfig.json")

```

### from dictionary

```python

my_config_dict = {"type_name" : "mysrc.datastructures.configs.a"}
my_config = ConfigParser().parse(my_config_dict)

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
my_config = ConfigParser().parse_typed(my_config_dict,a)

```

By default every field can be explicitly set to None. If you don't what this behaviour you can set the flag "allow_none" to False.

```python
    from cfgparser import settings
    settings.allow_none = False
```

## Features

- fully typed json and yaml configs
- nested configs
- complex union and optional types
- dict object into typed dataclass
- support for enums (string and int)

Whenever a Union type is encountered the parser tries to parse the config with the first type in the union. If this fails it tries the next type and so on. If all types fail the parser raises an exception.

## Installation

```bash
pip install cfgparser
```

## Features Roadmap

- specify config from cli
- post hock
- distributed configs
