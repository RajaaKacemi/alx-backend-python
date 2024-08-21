#!/usr/bin/env python3
"""Function with type annotations using TypeVar."""

from typing import Any, Mapping, TypeVar, Union

# Define a type variable that can be any type
T = TypeVar('T')


def safely_get_value(
        dct: Mapping[Any, T],
        key: Any,
        default: Union[T, None] = None
) -> Union[T, None]:
    """Returns for the given key if present, otherwise returns default."""
    if key in dct:
        return dct[key]
    return default
