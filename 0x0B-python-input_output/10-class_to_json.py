#!/usr/bin/python3
def class_to_json(obj):
    ''' return a dict of objects attributes'''
    return obj.__dict__
