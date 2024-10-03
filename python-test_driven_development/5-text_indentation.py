#!/usr/bin/python3
""" a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """ the function """
    limits = '.:?'
    if type(text) is not str:
        raise TypeError("text must be a string")
    for doc in limits:
        text = str(doc + '\n\n').join(b.strip() for b in text.split(doc))
    print(text, end='')
    if len(text) > 0 and text[-1] in limits:
        print('\n')
