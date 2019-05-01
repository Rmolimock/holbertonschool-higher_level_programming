#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
sign = ""
last = number % 10 if number > 0 else (number * -1) % 10
if last == 0:
    text = "and is 0"
elif last > 5:
    text = "and is greater than 5"
elif last < 6:
    text = "and is less than 6 and not 0"
if number < 0:
    sign = "-"
print("Last digit of {:d}".format(number), "is " + sign + "{:d}".format(last), text)
