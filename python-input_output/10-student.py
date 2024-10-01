#!/usr/bin/python3
""" student class"""


class Student:
    """ class student """
    def __init__(self, first_name, last_name, age):
        """ initialization"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrives dictionnar representation of student"""
        return self.__dict__

    def to_json(self, attrs=None):
        """ if attris is a list of str, only attribute name is retrived"""
        if attrs is None:
            return self.__dict__
        dictionary = {}
