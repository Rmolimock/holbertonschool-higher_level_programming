#!/usr/bin/python3
'''This module contains one function, print_square
'''
def print_square(size):
    '''print_square prints a square of '#'s of a give size
    '''
    if not isinstance(size, int) or size is None:
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    for y in range(size):
        for x in range(size):
            print("#", end="\n" if x == size - 1 else "")
