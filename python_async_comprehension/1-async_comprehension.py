#!/usr/bin/env python3
"""this module with afunction that uses asyncloops over async generator"""


import typing

async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> typing.List[float]:
    """a function that uses asyncloops over async generator"""
    return [i async for i in async_generator()]
