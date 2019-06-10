#!/usr/bin/python3
"""This module contains one class, Base"""


class Base():
    """Base class contains the number of instances,
    each of which are assigned an id in assending order"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
