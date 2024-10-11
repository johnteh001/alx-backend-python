#!/usr/bin/env python3
"""Duck Typing Module"""

from typing import Sequence, Iterable, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Function written using duck type"""

    return [(i, len(i)) for i in lst]
