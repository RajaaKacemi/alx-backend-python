#!/usr/bin/env python3
"""Function that takes an integer, returns an asyncio.Task"""

import asyncio

# Import wait_random from the specified module
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    Takes max_delay as an argument and returns an asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))
    return task
