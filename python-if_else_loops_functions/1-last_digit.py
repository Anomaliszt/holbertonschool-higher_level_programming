#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
last_digit = number
temp = 0

if last_digit < 0:
	last_digit = (-1) * last_digit
	temp = 2

last_digit = last_digit % 10

if temp == 2:
	last_digit = last_digit * (-1)


if number > 5:
	print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif number == 0:
	print(f"Last digit of {number} is {last_digit} and is 0")
else:
	print(f"Last digit of {number} is {last_digit} and is less than 6 and not 0")
