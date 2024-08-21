#!/usr/bin/env python3
""" takes floats as argument, returns sum as float"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """the returns sum as float"""
    return sum(mxd_lst)
