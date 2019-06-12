#!/usr/bin/python3
"""This module contains one class, Base"""


import json


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

    def to_json_string(list_dictionaries):
        if list_dictionaries is None or list_dictionaries == []:
            return '"[]"'
        elif not isinstance(list_dictionaries, list):
            raise TypeError('list_dictionaries must be a list of dicts')
        elif len(list_dictionaries) < 0:
            raise ValueError('list_dictionaries must contain dictionaries')
        elif not isinstance(list_dictionaries[0], dict):
            raise ValueError('list_dictionaries must contain dictionaries')
        else:
            return json.dumps(list_dictionaries)
