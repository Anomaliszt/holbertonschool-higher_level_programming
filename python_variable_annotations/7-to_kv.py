#!/usr/bin/env python3
"""Module that contains to_kv function"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns tuple of string and square of int/float"""
    return (k, float(v ** 2))