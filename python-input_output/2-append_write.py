#!/usr/bin/python3
"""
function that appends a string at the end of a text file (UTF8)
and returns the number of characters added:
"""


def append_write(filename="", text=""):
    """ The function """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
