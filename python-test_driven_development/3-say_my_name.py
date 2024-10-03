#!/usr/bin/python3
""" Python function that prints : my name is first name and last name """


def say_my_name(first_name, last_name=""):
    """ the function """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
