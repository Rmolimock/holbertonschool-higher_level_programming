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
        """returns JSON string representation of obj"""
        if list_dictionaries is None or len(list_dictionaries) is 0:
            return '[]'
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """save json file"""
        if list_objs is None:
            with open("{}.json".format(cls.__name__), "w") as f:
                f.write(to_json_string([]))
        else:
            tmp = []
            with open("{}.json".format(cls.__name__), "w") as f:
                for i in list_objs:
                    if issubclass(type(i), Base):
                        tmp.append(i.to_dictionary())
                f.write(Base.to_json_string(tmp))

    @staticmethod
    def from_json_string(json_string):
        """return deserialized list"""
        if json_string is None or len(json_string) is 0:
            return "[]"
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """create new instance of subclass using
        that class' update function
        """
        tmp = cls(1, 1)
        if tmp is not None:
            tmp.update(**dictionary)
        return tmp

    def load_from_file(cls):
        """create instances from a JSON file
        """
        new = []
        try:
            with open("{}.json".format(cls.__name__), "r") as f:
                tmp_dict = Base.from_json_string(f.read())
                for inst in tmp_dict:
                    new.append(cls.create(**inst))
                return new
        except Exception:
            return []
