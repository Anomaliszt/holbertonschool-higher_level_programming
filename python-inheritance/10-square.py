#!/usr/bin/python3
""" 3 classes, basegeometry, rectangle and square """


class BaseGeometry:
    """ class basegeometry"""
    def integer_validator(self, name, value):
        """ method that validates int for basegeometry"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class rectangle which inherits from BaseGeometry"""
    def __init__(self, width, height):
        """ method that initializes rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ method to use print function"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ method that returns area of rectangle"""
        return self.__width * self.__height


class Square(Rectangle):
    """ class square which inherits from rectangle"""
    def __init__(self, size):
        """ method that initializes square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ method that returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """ method to use print function"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
