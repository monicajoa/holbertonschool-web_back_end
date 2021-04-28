#!/usr/bin/env python3
"""[Multiple coroutines at the same time with async]
"""

from typing import List
import asyncio, random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """[Multiple coroutines at the same time with async]
    Args:
        n (int): [Number of iterations]
        max_delay (int): [Delay value, defaults to 10]
    Returns:
        list: [List of all the delays]
    """
    calls = []
    for i in range(n):
        calls.append(asyncio.create_task(wait_random(max_delay)))

    list_delays = []
    for delay in asyncio.as_completed(calls):
        tasks = await delay
        list_delays.append(tasks)

    return list_delays
