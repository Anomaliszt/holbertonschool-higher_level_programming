#!/usr/bin/python3
""" defines class square"""


class Square:
    """ Class Square """
    def __init__(self, size=0):
        """
        Method __init__: initialize data
        size: size of square
        """
        self.size = size

    @property
    def size(self):
        """ retrieve size """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size of data """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        return square area
        """
        return self.__size * self.__size
