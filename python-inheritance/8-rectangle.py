#!/usr/bin/python3
""" class validated by method """


class BaseGeometry:
    """ class BaseGeometry"""
    def area(self):
        """ method that returns area, not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ method that validates int for geometry"""
        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Rectangle class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initializes width and height with validation"""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
