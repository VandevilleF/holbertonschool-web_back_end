#!/usr/bin/env python3
"""An asynchronous coroutine"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays(float) in ascending order"""
    res = await asyncio.gather(*(wait_random(max_delay) for i in range(n)))
    return sorted(res)
