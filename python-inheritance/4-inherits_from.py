#!/usr/bin/python3
""" checks if obj is from class and if class of obj is not same class"""


def inherits_from(obj, a_class):
    """ return true if obj is from class and obj != a_class"""
    return isinstance(obj, a_class) and type(obj) is not a_class
