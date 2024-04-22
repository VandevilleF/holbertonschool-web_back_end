#!/usr/bin/env python3
"""A type-annotated function to_kv"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """a type-annotated func, that takes a 1st elem str k and the square
    of the int/float v and should be annotated as a float for 2ns elem
    as arguments and returns a tuple."""
    return (k, v * v)
