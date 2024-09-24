#!/usr/bin/python3

def inherits_from(obj, a_class):
    return isinstance(obj, a_class) and type(obj) is not a_class
