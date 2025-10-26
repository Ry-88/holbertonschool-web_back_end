#!/usr/bin/env python3
"""Module that contains an asynchronous comprehension coroutine.

This module imports async_generator and defines a coroutine that
uses asynchronous comprehension to collect random numbers generated
asynchronously.
"""

from typing import List
from async_generator import async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random float numbers from async_generator.

    This coroutine uses an asynchronous comprehension to iterate over
    async_generator and gather 10 random numbers into a list, which is
    then returned.

    Returns:
        List[float]: A list of 10 random float numbers between 0 and 10.
    """
    return [i async for i in async_generator()]
