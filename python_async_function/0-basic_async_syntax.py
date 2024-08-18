#!/usr/bin/env python3
'''simple asynchrone method'''
import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    '''waits for a random delay between 0 and input
    parameter then returns the delay as a float'''
    random_delay = uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay
