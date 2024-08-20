#!/usr/bin/env python3
'''asynchio generator function'''
import asyncio
from random import uniform


async def async_generator():
    '''loops 10 time then yield a random number between 0 and 10'''
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)
