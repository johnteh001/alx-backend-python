#!/usr/bin/env python3
"""Runtime Comprehensions"""

import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Function measures total time for async_comprehension call"""
    start: float = time.perf_counter()
    result = await asyncio.gather(*[asyncio.create_task(async_comprehension())
                                  for i in range(4)])
    total_time: float = time.perf_counter() - start
    return total_time
