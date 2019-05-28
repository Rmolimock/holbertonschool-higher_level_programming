#!/usr/bin/python3
'''This module contains the add_integer function
'''


def add_integer(a, b=98):
    '''add_integer adds two integers and/or floats together
    and returns an integer of their sum
    '''
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
