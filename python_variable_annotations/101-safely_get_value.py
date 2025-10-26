#!/usr/bin/env python3
"""Module that defines a function to safely
retrieve a value from a dictionary."""

from typing import Mapping, TypeVar, Any, Union

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Union[T, None] = None
) -> Union[T, None]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary to get the value from.
        key (Any): The key to search for.
        default (Union[T, None], optional): The default
        value to return if the key
            does not exist. Defaults to None.

    Returns:
        Union[T, None]: The value associated with the key if it exists,
        otherwise the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
