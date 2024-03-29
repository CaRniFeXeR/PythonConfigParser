from dataclasses import dataclass
from typing import List, Optional, Tuple
from enum import Enum


@dataclass
class DummyConfigElement:
    name: str
    list: List[int]
    another_list: List[float]


class DummyEnum(Enum):
    RED = 1
    BLUE = 2
    ORANGE = 27


@dataclass
class DummyEnumConfig:
    name: str
    enum: DummyEnum


@dataclass
class DummyConfig:
    config_name: str
    dummy_element: DummyConfigElement
    dummy_element_list: List[DummyConfigElement]
    second_dummy_element: DummyConfigElement = DummyConfigElement(
        "dummy_config el", [1], [0.4, 0.5])


@dataclass
class NestedDummyConfig:
    dummy_conf_a: DummyConfig
    dummy_conf_b: DummyConfig
    main_element: DummyConfigElement


@dataclass
class DummyOptionalFieldsConfig:
    config_name: str
    optional_el: Optional[DummyConfigElement] = None
    optional_list: Optional[List[float]] = None


@dataclass
class DummyTupleConfig:
    config_name: str
    min_max: Tuple[float, float]
    from_to_time: Tuple[int, str, int, str]
