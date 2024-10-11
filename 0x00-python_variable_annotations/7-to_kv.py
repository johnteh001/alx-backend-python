#!/usr/bin/env python3
"""Complex Types"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Function returns a tuple"""

    ret: float = v*v
    return (k, ret)
