#!/usr/bin/env python3
"""Module that defines a function to safely
retrieve a value from a dictionary."""

from typing import TypeVar, Mapping, Any, Optional

T = TypeVar('T')


def safely_get_value(
    dct: Mapping[Any, T],
    key: Any,
    default: Optional[T] = None
) -> Optional[T]:
    """
    Safely retrieve a value from a dictionary.

    Args:
        dct (Mapping[Any, T]): The dictionary
        or mapping to retrieve the value from.
        key (Any): The key to look up in the dictionary.
        default (Optional[T], optional): The value to
        return if the key is not found.
        Defaults to None.

    Returns:
        Optional[T]: The value associated with the key
        if found, otherwise the default.
    """
    if key in dct:
        return dct[key]
    else:
        return default
