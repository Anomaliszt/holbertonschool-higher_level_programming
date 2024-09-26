#!/usr/bin/python3
""" create class that extends the built in iterator"""


class CountedIterator:
    """class CountedIterator """
    def __init__(self, data):
        """ method that initializes CountedIterator """
        self.data = iter(data)
        self.count = 0

    def get_count(self):
        """ methdo that returns count"""
        return self.count

    def __next__(self):
        """ method that overides next """
        try:
            item = next(self.data)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration
