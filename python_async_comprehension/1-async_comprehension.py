#!/usr/bin/env python3
"""A coroutine called async_comprehension"""
import asyncio

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension():
    """collect 10 random numbers using an async comprehensing
    over async_generator, then return the 10 random numbers."""
    collect_random = []
    async for i in async_generator():
        collect_random.append(i)
    return collect_random
