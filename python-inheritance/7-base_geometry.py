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
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
