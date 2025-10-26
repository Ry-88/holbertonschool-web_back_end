#!/usr/bin/env python3
"""Module that defines a function for safely
returning the first element of a list."""

from typing import Any, Sequence, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Return the first element of a sequence if it exists, otherwise None.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple)
        of unknown element types.

    Returns:
        Optional[Any]: The first element if available, otherwise None.
    """
    if lst:
        return lst[0]
    else:
        return None
