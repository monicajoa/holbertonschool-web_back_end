#!/usr/bin/env python3
"""[Iterable object]
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """[Function Iterable]

    Args:
        lst (Iterable[Sequence]): [Iterable sequence list]

    Returns:
        List[Tuple[Sequence, int]]: [Iterable sequence list of integers]
    """
    return [(i, len(i)) for i in lst]
