#!/usr/bin/env python3
"""Measure the runtime"""

import time
import asyncio
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function Measures runtime
    Args:
        n: argument 1
        max_delay: argument 2
    Returns:
        total_time / n(float): quotient of time elapsed and n
    """
    start: float = time.perf_counter()
    trial: List[float] = asyncio.run(wait_n(n, max_delay))
    total_time = time.perf_counter() - start
    return total_time / n
