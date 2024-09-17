#!/usr/bin/python3
""" defines square class"""


class Square:
    """ Class Square"""
    def __init__(self, size=0):
        """
        Method __init__: Initialize data
        size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        returns square area
        """
        return self.__size * self.__size
