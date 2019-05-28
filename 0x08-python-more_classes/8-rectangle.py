#!/usr/bin/python3
'''This module contains one class, Rectangle.
'''

class Rectangle():
    '''Rectangle has a width/height, area, perimeter
    prints out as a block of given characters, prints when deleted,
    tracks the number of rectangle instances, compares two
    Rectangle instance areas
    '''
    number_of_instances = 0
    print_symbol = "#"
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        self.__class__.number_of_instances += 1
    def __str__(self):
        ret = ''
        if self.width == 0 or self.height == 0:
            return ret
        for y in range(self.height):
            for x in range(self.width + 1):
                ret += '\n' if x == self.width else str(self.print_symbol)
        return ret
    def __repr__(self):
        return 'Rectangle({}, {})'.format(self.__width, self.__height)
    def __del__(self):
        self.__class__.number_of_instances -= 1
        print('Bye rectangle...')
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
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        return rect_2 if rect_2.area() > rect_1.area() else rect_1
