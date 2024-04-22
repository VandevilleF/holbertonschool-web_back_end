#!/usr/bin/env python3
"""A type-annotated function element_length"""
from typing import List, Iterable, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains an elem from the input list and its length."""
    return [(i, len(i)) for i in lst]
