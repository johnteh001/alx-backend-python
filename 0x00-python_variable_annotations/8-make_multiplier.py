#!/usr/bin/env python3
"""Make_Multiplier Module"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Function returns a callback function"""

    def F(num: float) -> float:
        """Function returns a float"""
        return multiplier * num
    return F
