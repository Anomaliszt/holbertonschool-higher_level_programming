#!/usr/bin/python3
""" create abstract class Shape """


from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """ abstract class Shape """
    @abstractmethod
    def area(self):
        """ method that returns area """
        pass

    @abstractmethod
    def perimeter(self):
        """ method that returns perimeter"""
        pass


class Circle(Shape):
    """ Subclass of shape"""
    def __init__(self, radius):
        """ method that initializes circle"""
        self.radius = radius

    def area(self):
        """ method that returns area of circle"""
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        """ method that returns perimeter of circle"""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """ subclass of shape """
    def __init__(self, width, height):
        """ method that initializes Rectangle"""
        self.width = width
        self.height = height

    def area(self):
        """ method that returns area of rectangle"""
        return self.width * self.height

    def perimeter(self):
        """ method that returns perimeter """
        return 2 * (self.width + self.height)


def shape_info(arg):
    """ give info of shape"""
    print("Area: {}".format(arg.area()))
    print("Perimeter: {}".format(arg.perimeter()))
