#!/usr/bin/env python3
"""Module that contains an asynchronous generator coroutine.

This module defines a coroutine that yields random numbers
asynchronously, demonstrating how to use async generators
in Python for concurrent operations.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously yield random float numbers between 0 and 10.

    This coroutine loops 10 times, each time asynchronously waiting
    for 1 second before yielding a random float number between 0 and 10.
    Yields:
        float: A random number between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
