#!/usr/bin/env python3
"""Tasks"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Asynchronous routine that takes 2 integer arguments"""
    tasks = []

    for _ in range(n):
        # Agregamos 'n' veces a la lista 'tasks' las corrutinas creadas
        # por 'wait_random'
        tasks.append(wait_random(max_delay))

    # Luego ejecutamos las tareas simultaneamente con 'asyncio.gather' la
    # lista 'tasks' y lo almacenamos en una variable
    resultados = await asyncio.gather(*tasks)
    # Finalmente ordenamos la lista de resultados con 'sorted'
    return sorted(resultados)
