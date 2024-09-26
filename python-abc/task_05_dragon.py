#!/usr/bin/python3
""" designing two mixin classes"""


class SwimMixin:
    """ Mixin class Swim """
    def swim(self):
        """ function that prints """
        print("The creature swims!")

class FlyMixin:
    """ Mixin class Fly """
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
