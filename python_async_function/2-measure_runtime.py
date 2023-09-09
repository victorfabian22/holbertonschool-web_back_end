#!/usr/bin/env python3
"""Let's execute multiple coroutines at the same time with async"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Function that measures the time of a concurrent function"""
    inicio = time.time()
    asyncio.run(wait_n(n, max_delay))
    fin = time.time()
    total = fin - inicio
    return total / n
