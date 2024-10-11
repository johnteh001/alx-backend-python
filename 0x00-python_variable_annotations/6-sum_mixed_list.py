#!/usr/bin/env python3
"""Mixed list Module"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Summation function
    Return:
        summation(float): summation of list
    """
    summation: float = 0
    for i in mxd_list:
        summation += i
    return summation
