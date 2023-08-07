
from typing import Type
import typing


def is_union_type(type: Type) -> bool:
    """
    checks if the given type is a union type
    """
    return typing.get_origin(type) == typing.Union
