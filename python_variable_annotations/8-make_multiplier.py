#!/usr/bin/env python3
"""A type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """A type-annotated func, that takes a float multiplier
    as arg and returns a func that multiplies a float by multiplier."""
    def multiplier_func(n: float) -> float:
        """A type-annotated func, that multiplies"""
        return (n * multiplier)
    return multiplier_func
