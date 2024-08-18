#!/usr/bin/env python3
"""Measure the runtime"""

import asyncio
from typing import List
from time import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Measures the total execution time for wait_n(n, max_delay)"""
    start = time()
    asyncio.run(wait_n(n, max_delay))
    end = time()
    return (end - start) / n
