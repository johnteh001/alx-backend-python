#!/usr/bin/env python3
"""Task 4"""

import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Functio calls task_wait_random function
    Args:
        n: number of times to spawn task_wait_random function
        max_delay: argument passed to task_wait_random function
    Returns:
        delay_list (List[float]): delay list
    """
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []
    for _ in range(n):
        tasks.append(task_wait_random(max_delay))
    delay_list = [await task for task in asyncio.as_completed(tasks)]
    return delay_list
