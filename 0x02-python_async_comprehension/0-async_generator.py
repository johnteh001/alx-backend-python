#!/usr/bin/env python3
"""Async Generator"""

import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator:
    """Function yields random values between 0 and 1"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
