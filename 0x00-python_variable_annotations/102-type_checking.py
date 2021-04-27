#!/usr/bin/env python3
"""[Type Checking]
"""

from typing import List, Tuple
from math import floor


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """[Function with others type Annotations and
    return values with the appropriate types]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, floor(3.0))
