#!/usr/bin/env python3
"""A type-annotated function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """A type-annotated function sum_mixed_list which takes a list
    mxd_lst of int and floats and returns their sum as a float."""
    return sum(mxd_lst)
