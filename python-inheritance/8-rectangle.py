#!/usr/bin/python3
""" 2 classes with one that inherits from parent"""


class BaseGeometry:
    """ class baseGeometry """
    def integer_validator(self, name, value):
        """ method that validates int for geometry"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ class rectangle that inherits from basegeometry"""
    def __init__(self, width, height):
        """method that initializes rectangle """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
