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
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        '''save a list of dictionaries of objects in list_objs
        to a json file'''
        if list_objs is None:
            with open("{}.json".format(cls.__name__), "w") as f:
                f.write(to_json_string([]))
        elif not isinstance(list_objs, list):
            raise TypeError('list_obj must be a list')
        else:
            list_dicts = []
            with open("{}.json".format(cls.__name__), "w") as f:
                for obj in list_objs:
                    if issubclass(type(obj), Base):
                        list_dicts.append(obj.to_dictionary())
                    else:
                        raise TypeError('list_dicts must be a list of objects')
                f.write(Base.to_json_string(list_dicts))
