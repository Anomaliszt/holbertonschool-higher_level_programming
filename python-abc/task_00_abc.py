#!/usr/bin/env python3
""" create abstract class """

from abc import ABC, abstractmethod


class Animal(ABC):
    """ abstract class Animal """
    @abstractmethod
    def sound(self):
        """ function that defines sound of animal"""
        pass


class Dog(Animal):
    """ Subclass of animal """
    def sound(self):
        """ method that defines sound of animal """
        return "Bark"


class Cat(Animal):
    """ Subclass of animal"""
    def sound(self):
        """ method that denies sound of animal """
        return "Meow"
