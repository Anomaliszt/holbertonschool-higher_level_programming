#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = (-1) * number
    last = number % 10
    print(last, end="")
    return last
