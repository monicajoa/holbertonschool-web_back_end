#!/usr/bin/env python3.7
"""[The basics of async]
"""

import asyncio
import random


async def wait_random(max_delay=10):
    """[Asynchronous coroutine that takes in an integer argument]

    Args:
        max_delay (int, optional): [Delay value]. Defaults to 10.

    Returns:
        [Float]: [New random delay value]
    """
    rnd_num = random.uniform(0, max_delay)
    await asyncio.sleep(rnd_num)
    return rnd_num
