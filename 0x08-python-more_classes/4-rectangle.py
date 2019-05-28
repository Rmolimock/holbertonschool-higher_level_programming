#!/usr/bin/python3
'''This module contains one class, Rectangle.
'''

class Rectangle():
    '''Rectangle has a width/height, area, perimeter
    and prints out as a block of '#'s
    '''
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    def __str__(self):
        ret = ''
        if self.width == 0 or self.height == 0:
            return ret
        for y in range(self.height):
            for x in range(self.width):
                ret += '\n' if x == self.width - 1 else '#'
        return ret
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
    @property
    def width(self):
        return self.__width
    @property
    def height(self):
        return self.__height
    @width.setter
    def width(self, width):
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        elif width < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = width
    @height.setter
    def height(self, height):
        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        elif height < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = height
    def area(self):
        return self.width * self.height
    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)
