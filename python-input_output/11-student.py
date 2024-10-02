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
        dict = {}
        for i in attrs:
            if i in self.__dict__.keys():
                dict[i] = self.__dict__[i]
        return dict

    def reload_from_json(self, json):
        """function that replaces all attributes of the Student instance """
        for key, value in json.items():
            setattr(self, key, value)
