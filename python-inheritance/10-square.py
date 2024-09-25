#!/usr/bin/python3
""" 3 classes, basegeometry, rectangle and square """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class square which inherits from rectangle"""
    def __init__(self, size):
        """ method that initializes square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """ method that returns area of square"""
        return self.__size ** 2

    def __str__(self):
        """ method to use print function"""
        return "[Rectangle] {}/{}".format(self.__size, self.__size)
