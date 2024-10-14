#!/usr/bin/env python3
"""Basic Async Coroutine"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Function waits for a random delay
    Returns:
        wait(float): dalay time
    """
    wait: float = random.uniform(0, max_delay)
    await asyncio.sleep(wait)
    return wait
