#!/usr/bin/env python3
"""Measures the total execution time for wait_n(n, max_delay)."""
import random
import asyncio
from typing import List
import time

wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measures the execution time for wait_n and returns average time per task.
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start
    return elapsed / n
