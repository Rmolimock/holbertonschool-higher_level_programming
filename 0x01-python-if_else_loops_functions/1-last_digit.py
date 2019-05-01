#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
tmp = number
if number < 0:
    number = -(number)
last = number % 10
if tmp < 0:
    number = tmp
    last = -(last)

if last > 5:
    text = "and is greater than 5"
elif last == 0:
    text = "and is 0"
elif last < 6:
    text = "and is less than 6 and not 0"

print("Last digit of {:d} is {:d}".format(number, last), text)
