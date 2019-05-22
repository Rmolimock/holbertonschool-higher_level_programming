#!/usr/bin/python3
''' square with area method and setter/getter for size'''


class Square:
    def __init__(self, size=0):
        if size is not None:
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if value is not None:
            if not isinstance(value, int):
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

    def area(self):
        if self.__size is None:
            return None
        else:
            return self.__size * self.__size
