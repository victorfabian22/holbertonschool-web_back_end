#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """coroutine that will execute async_comprehension four
       times in parallel using asyncio.gather."""
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(async_comprehension(),
                         async_comprehension(),
                         async_comprehension(),
                         async_comprehension())
    end_time = asyncio.get_event_loop().time()
    total_runtime = end_time - start_time
    return total_runtime
