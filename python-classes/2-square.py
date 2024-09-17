#!/usr/bin/python3
"""
This module defines a class Square with a size attribute.

Classes:
	Square: defined class with private size attribute.

Methods:
	__init__(self, size): Init the size of square.
"""
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size mut be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
