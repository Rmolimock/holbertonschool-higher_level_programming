#!/usr/bin/python3
def fizzbuzz():
    for n in range(1, 101):
        if not n % 3 and not n % 5:
            print("FizzBuzz", end=" ")
        elif not n % 3:
            print("Fizz", end=" ")
        elif not n % 5:
            print("Buzz", end=" ")
        else:
            print("{}".format(n), end=" ")
