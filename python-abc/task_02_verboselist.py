#!/usr/bin/python3
""" abstract class that extends Python list Class"""


from abc import ABC, abstractmethod
import math


class VerboseList(list):
    """ class VerboseList"""
    def append(self, item):
        """ override append method with printed message """
        super().append(item)
        print("Added {} to the list.".format(item))

    def extend(self, x):
        """ override extend method with printed message """
        super().extend(x)
        print("Extended the list with {} items.".format(len(x)))

    def remove(self, item):
        """ override remove method with printed message."""
        super().remove(item)
        print("Removed {} from the list.".format(item))

    def pop(self, index=-1):
        """ override pop method with printed message."""
        item = super().pop(index)
        print("Popped {} from the list.".format(item))
        return item
