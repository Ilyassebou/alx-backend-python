#!/usr/bin/env python3
"""Creates a generator"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """Asynchronously yields a random float between 0 and 10, 
    every second for 10 iterations"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)

