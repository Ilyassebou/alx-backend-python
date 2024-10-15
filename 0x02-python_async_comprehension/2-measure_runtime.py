#!/usr/bin/env python3
""" Run time for four parallel comprehensions """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ 
    Asynchronous function that measures and returns the runtime of
    running 4 instances of the async_comprehension function.

    Returns:
        float: The runtime of the async_comprehension function in seconds.
    """
    start = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    totalRuntime = time.perf_counter() - start
    return totalRuntime
