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

    @classmethod
    def save_to_file(cls, list_objs):
        if not isinstance(list_objs, list):
            raise TypeError('list_objs must be a list of objects')
        obj_class = list_objs[0].__class__
        if not obj_class == cls:
            raise TypeError('objects in list_objs must be same type')
        list_dicts = []
        for obj in list_objs:
            if not type(obj) == obj_class:
                raise TypeError('objects in list_objs must be of same type')
            else:
                obj_dict = obj.to_dictionary()
                list_dicts.append(obj_dict)
        json_string = cls.to_json_string(list_dicts)
        filename = type(list_objs[0]).__name__ + '.json'
        with open(filename, mode="w+", encoding="utf-8") as f:
            return f.write(json_string)
