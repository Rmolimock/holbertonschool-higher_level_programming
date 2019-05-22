#!/usr/bin/python3
''' square with size that must be int > 0'''


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size is not None:
            self.__size = size
