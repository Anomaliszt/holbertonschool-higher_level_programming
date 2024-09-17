#!/usr/bin/python3
"""
This module defines a class Square with size validation.

Classes:
	Square: class deined square with pruvate size
                and validates the size during init

Methods:
	__init__(self, size=0): Init square with size.

Raises:
	TypeError: If size is not an int
	ValueError: If size is less than zero
"""
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size * self.__size
