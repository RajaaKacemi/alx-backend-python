#!/usr/bin/env python3
"""A coroutine called async_generator that """
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    collects 10 random numbers using async comprehension,
    """
    result = [i async for i in async_generator()]
    return result
