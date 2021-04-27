#!/usr/bin/env python3
"""[Complex types - Functions]
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """[Type-annotated function that takes a float multiplier as arg]

    Args:
        multiplier (float): [Floating number]

    Returns:
        Callable[[float], float]: [fn that multiplies a float by multiplier]
    """
    def multiplies(number: float) -> float:
        """[Function that multiplies a float by multiplier]

        Args:
                number (float): [Floating number]

        Returns:
                float: [the multiplication of a floating number and multiplier]
        """
        return number * multiplier
    return multiplies
