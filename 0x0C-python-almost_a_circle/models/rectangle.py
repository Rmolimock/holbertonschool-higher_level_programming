#!/usr/bin/python3
'''This module contains one class, Rectangle'''


from models.base import Base


class Rectangle(Base):
    '''Rectangle has a height/width and x/y position'''
    print_symbol = '#'

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        elif value < 1:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        elif value < 1:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.x, self.y, self.width, self.height)

    def area(self):
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width * self.height

    def display(self):
        ret = ''
        if self.width == 0 or self.height == 0:
            print(ret)
        for y_pos in range(self.y):
            ret += '\n'
        for y in range(self.height):
            for x_pos in range(self.x):
                ret += ' '
            for x in range(self.width + 1):
                ret += '\n' if x == self.width else str(self.print_symbol)
        print(ret, end="")
