#!/usr/bin/python3
'''This module contains one function, say_my_name
'''
def say_my_name(first_name, last_name=""):
    '''say_my_name prints a string containing first_name and an optional
    last_name
    '''
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    elif last_name and not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    elif last_name is None:
        raise TypeError("last_name must be a string")
    else:
        print("My name is {} {}".format(first_name, last_name))
