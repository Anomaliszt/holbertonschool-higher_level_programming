#!/usr/bin/python3
""" prints sorted list"""


class MyList(list):
    """ class MyList inherinted from list"""
    def print_sorted(self):
        """ method that prints sorted object"""
        print(sorted(self))
