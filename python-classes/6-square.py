#!/usr/bin/python3
""" Class Square """


class Square:
    """ Square Class """
    def __init__(self, size=0, position=(0, 0)):
        """
        Method __init__: initialize data
        size: size of square
        position: given position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """ retrieve size of Square """
        return self.__size

    @size.setter
    def size(self, value):
        """ set size """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ retrieve position """
        return self.__position

    @position.setter
    def position(self, value):
        """ set position """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ retrieve area size """
        return self.__size * self.__size

    def my_print(self):
        """ print square and print space based on position and size """
        if self.__size == 0:
            print("")
            return
        for i in range(self.__position[1]):
            print()
        for row in range(self.__size):
            for i in range(self.__position[0]):
                print(" ", end="")
            for line in range(self.__size):
                print("#", end="")
            print()
