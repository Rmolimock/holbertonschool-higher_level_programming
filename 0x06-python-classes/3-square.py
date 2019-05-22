#!/usr/bin/python3
''' square with a method for finding the area  '''


class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        elif size is not None:
            self.__size = size

    def area(self):
        if self.__size is not None:
            return self.__size * self.__size
        else:
            return None
