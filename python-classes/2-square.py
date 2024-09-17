#!/usr/bin/python3
""" defines class square """


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """
        Method __init__: initialize data
        size: size of square
        """
        if not isinstance(size, int):
            raise TypeError("size mut be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
