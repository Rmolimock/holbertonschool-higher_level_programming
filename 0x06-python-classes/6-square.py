#!/usr/bin/python3
''' square that prints itself at a given position '''


class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.position = position

    @property
    def size(self):
        return self.__size

    @property
    def position(self):
        return self.__position

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if value:
            if not isinstance(value, tuple):
                raise TypeError("position must be a tuple of 2 " +
                                "positive integers")
            elif value[0] < 0 or value[1] < 0:
                raise TypeError("position must be a tuple of 2 "
                                "positive integers")
            self.__position = value

    def area(self):
        if self.__size is not None:
            return self.__size * self.__size
        else:
            return None

    def my_print(self):
        for i in range(self.__position[1]):
                    print()
        for y in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for i in range(self.__size):
                print("#", end="")
            print()
        if self.__size == 0:
            print()
