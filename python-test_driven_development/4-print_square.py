#!/usr/bin/python3
""" function that prints a square with the character # """


def print_square(size):
    """ The Function """
    if type(size) is not int:
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for row in range(size):
            for column in range(size):
                print("#", end="")
            print("")
