#!/usr/bin/python3
""" rectangle class that returns area and perimeter """


class Rectangle:
    """ Define Rectangle """
    def __init__(self, width=0, height=0):
        """ initialize rectangle """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ getter for width """
        return self.__width

    @width.setter
    def width(self, value):
        """ setter for width """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ getter for height """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter for height """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ func that returns area of rectangle """
        return self.__height * self.__width

    def perimeter(self):
        """ func that returns perimeter of rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.width * 2)

    def __str__(self):
        """ function for printing"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for row in range(self.__height):
            for line in range(self.__width):
                str += "#"
            str += "\n"
        return str[:-1]
