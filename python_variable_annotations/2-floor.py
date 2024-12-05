#!/usr/bin/env python3
"""Module that contains floor function"""


def floor(n: float) -> int:
    """Returns floor of float number"""
    return int(n) if n >= 0 else int(n) - 1