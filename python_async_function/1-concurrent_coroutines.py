#!/usr/bin/env python3
'''multiple coroutines'''
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''double awaiting'''
    task = []
    for _ in range(n):
        task.append(wait_random(max_delay))
    result = await asyncio.gather(*task)
    return sorted(result)
