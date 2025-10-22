#!/usr/bin/env python3
"""
Module 1-concurrent_coroutines
Defines an asynchronous routine wait_n that spawns multiple coroutines
concurrently using wait_random from a previous module.
"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawn wait_random n times with the specified max_delay and return
    a list of all the delays (float values) in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order, without using sort().
    """
    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    sorted_delays = []

    for delay in delays:
        # Insert delay in ascending order manually (no sort())
        inserted = False
        for i in range(len(sorted_delays)):
            if delay < sorted_delays[i]:
                sorted_delays.insert(i, delay)
                inserted = True
                break
        if not inserted:
            sorted_delays.append(delay)

    return sorted_delays
