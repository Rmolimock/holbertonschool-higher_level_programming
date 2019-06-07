#!/usr/bin/python3
class Student():
    '''Student has a first/last name and age
    '''
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        elif isinstance(attrs, list):
            new = {}
            for s in attrs:
                if isinstance(s, str) and s in self.__dict__:
                    new[s] = self.__dict__[s]
            return new
