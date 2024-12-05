#!/usr/bin/env python3
"""Module that contains make_multiplier function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def multiply(n: float) -> float:
        return multiplier * n
    return multiply