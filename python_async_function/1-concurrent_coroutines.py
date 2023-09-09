#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import random
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that takes 2 integer arguments"""
    tasks = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    resultados = await asyncio.gather(*tasks)
    return sorted(resultados)
