from dataclasses import dataclass
from typing import List, Optional


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

@dataclass
class NestedDummyConfig:
    dummy_conf_a : DummyConfig
    dummy_conf_b : DummyConfig
    main_element : DummyConfigElement

@dataclass
class DummyOptionalFieldsConfig:
    config_name: str
    optional_el: Optional[DummyConfigElement] = None
    optional_list : Optional[List[float]] = None
