#!/usr/bin/env python3
"""[Complex types - Mixed list]
"""

from typing import List, Union
Var = Union[int, float]


def sum_mixed_list(mxd_lst: List[Var]) -> float:
    """[Type-annotated function which takes a list of integers and floats]

    Args:
        mxd_lst (List[Var]): [List of integers and floats]

    Returns:
        float: [Their sum as a float]
    """
    return sum(mxd_lst)
