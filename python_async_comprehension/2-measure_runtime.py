#!/usr/bin/env python3
"""A coroutine called measure_runtime"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> int:
    """ Execute async_comprehension four times in parallel
    using asyncio.gather"""
    start = time.time()
    await asyncio.gather(*(async_comprehension() for i in range(4)))
    elapse = (time.time() - start)
    return elapse
