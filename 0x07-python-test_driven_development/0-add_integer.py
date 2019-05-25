#!/usr/bin/python3
'''This module contains the add_integer function
'''


def add_integer(a, b=98):
    '''add_integer adds two integers and/or floats together
    and returns an integer of their sum
    '''
    if not type(a) is int and not type(a) is float:
        raise TypeError("{} must be an integer".format(a))
    if not type(b) is int and not type(b) is float:
        raise TypeError("{} must be an integer".format(b))
    return int(a) + int(b)
