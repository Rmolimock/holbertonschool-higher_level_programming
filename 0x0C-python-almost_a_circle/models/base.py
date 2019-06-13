#!/usr/bin/python3
"""This module contains the base class
"""
import json


class Base:
    """This is the base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string returns json string of dicts in list_dicts"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save json representation of objects in list_objs into a file'''
        with open("{}.json".format(cls.__name__), "w") as f:
            if list_objs is None:
                    f.write(to_json_string([]))
            else:
                    f.write(Base.to_json_string([x.to_dictionary()
                                                 for x in list_objs]))
