#!/usr/bin/env python3
"""[Complex types - List of floats]
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """[Type-annotated function which takes a list of floats as argument]

    Args:
        input_list (List[float]): [Floating number list]

    Returns:
        float: [Their sum as a float]
    """
    return sum(input_list)
