#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number == 0:
    text = "is zero"
elif number > 0:
    text = "is positive"
else:
    text = "is negative"
print("{:d}".format(number), text)

