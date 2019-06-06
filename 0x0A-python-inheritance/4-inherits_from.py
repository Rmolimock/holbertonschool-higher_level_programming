#!/usr/bin/python3
def inherits_from(obj, a_class):
    '''checks if object isinstance of subclass of a_class'''
    return issubclass(type(obj), a_class) and type(obj) is not a_class
