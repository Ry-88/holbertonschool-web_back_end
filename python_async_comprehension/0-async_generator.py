#!/usr/bin/env python3
"""Asynchronous generator module."""

import asyncio
import random


async def async_generator():
    """
    Asynchronously yield random numbers.

    This coroutine loops 10 times, each time asynchronously waiting
    for 1 second before yielding a random float between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
