#!/usr/bin/env python3
"""Duck Type First Sequence"""


from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Duck Typing First Element of Sequence
    Returns: list or None
    """
    if lst:
        return lst[0]
    else:
        return None
