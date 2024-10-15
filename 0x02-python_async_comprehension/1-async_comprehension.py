#!/usr/bin/env python3
"""Async Comprehesions"""

import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Function uses generator
    Returns:
        result (List[float]): list of floats
    """
    return [i async for i in async_generator()]
