#!/usr/bin/env python3
"""The basics of async"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """coroutine with an integer parameter"""
    var = random.uniform(0, max_delay)
    await asyncio.sleep(var)
    return var


async def main():
    """principal function"""
    ran = await wait_random()


asyncio.run(main())
