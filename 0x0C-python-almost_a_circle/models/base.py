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
        with open("{}.json".format(cls.__name__), "w+", encoding='utf-8') as f:
            if list_objs is None or list_objs == []:
                    f.write(Base.to_json_string([]))
            else:
                    f.write(Base.to_json_string([obj.to_dictionary()
                                                 for obj in list_objs]))

    def from_json_string(json_string):
        '''convert json string of obj dicts into list of same'''
        if json_string is None or json_string == "":
            return []
        else:
            return json.loads(json_string)
