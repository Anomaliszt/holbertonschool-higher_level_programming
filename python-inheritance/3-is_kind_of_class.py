#!/usr/bin/python3
""" check if object is instance of class"""


def is_kind_of_class(obj, a_class):
    """ method that checks if obj is from class"""
    if isinstance(obj, a_class):
        return True
    return False
