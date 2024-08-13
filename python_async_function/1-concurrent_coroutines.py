#!/usr/bin/env python3
'''multiple coroutines'''
wait_random = __import__("0-basic_async_syntax").wait_random
import asyncio


async def wait_n(n, max_delay):
    '''double awaiting'''
    task = []
    for _ in range(n):  
        task.append(wait_random(max_delay))
    result = await asyncio.gather(*task)
    return result
