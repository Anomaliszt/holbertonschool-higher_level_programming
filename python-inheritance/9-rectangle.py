#!/usr/bin/python3
""" 2 classes with one parent and one that inherits"""


class BaseGeometry:
    """ class basegeometry wich validates int"""
    def integer_validator(self, name, value):
        """ method that validates int for geometry"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class rectangle that inherits from base geometry """
    def __init__(self, width, height):
        """ method that initializes rectangle"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """ method str to use print"""
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """ method that returns area of rectangle"""
        return self.__width * self.__height
