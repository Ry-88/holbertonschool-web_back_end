#!/usr/bin/env python3
"""this module with afunction that measure run time of 4 tasks
done concurrency"""


import asyncio
import time

async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """a function that measure run time of 4 tasks done concurrency"""
    start = time.perf_counter()
    tasks = [async_comprehension() for i in range(4)]
    await asyncio.gather(*tasks)
    return time.perf_counter() - start
