#!/usr/bin/python3
'''instantiate with private size'''


class Square:
    def __init__(self, size=0):
        if size is not None:
            self.__size = size
