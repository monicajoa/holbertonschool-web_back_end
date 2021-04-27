#!/usr/bin/env python3
"""[Complex types - String and int/float to tuple]
"""

from typing import Tuple, Union

Var = Union[int, float]


def to_kv(k: str, v: Var) -> Tuple[str, float]:
    """[type-annotated function that takes a str and an int OR float as args]

    Args:
        k (str): [First element of the tuple]
        v (Var): [Second element the square of the int/float]

    Returns:
        Tuple[str, float]: [Tuple annotated as str and float]
    """
    return (k, v*v)
