#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = number
temp = 0

if digit < 0:
    digit = (-1) * digit
    temp = 2

digit = digit % 10

if temp == 2:
    digit = digit * (-1)


if number > 5:
    print(f"Last digit of {number} is {digit} and is greater than 5")
elif number == 0:
    print(f"Last digit of {number} is {digit} and is 0")
else:
    print(f"Last digit of {number} is {digit} and is less than 6 and not 0")
