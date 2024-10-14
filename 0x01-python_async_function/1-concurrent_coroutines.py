#!/usr/bin/env python3
""" Multiple Coroutines"""

import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Function returns a list of all delays
    Args:
        n (int): number of times to spawn wait_random
        max_delay (int): delay
    Returns:
        delay_list (List[list]): list of delays in ascending order
    """
    delay_list: List[float] = []
    tasks: List[asyncio.Task] = []
    for _ in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    delay_list = [await task for task in asyncio.as_completed(tasks)]
    return delay_list
