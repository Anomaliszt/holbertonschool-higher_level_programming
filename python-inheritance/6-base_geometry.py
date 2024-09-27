#!/usr/bin/python3
""" class with exception"""


class BaseGeometry:
    """ Class BaseGeometry"""
    def area(self):
        """ method area of geometry"""
        raise Exception("area() is not implemented")
