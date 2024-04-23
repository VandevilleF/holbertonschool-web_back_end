#!/usr/bin/env python3
"""A coroutine called async_comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers."""
    collect_random = [rd_nb async for rd_nb in async_generator()]
    return collect_random
