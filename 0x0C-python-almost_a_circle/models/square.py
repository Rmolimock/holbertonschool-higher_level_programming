#!/usr/bin/python3
'''This module contains one class, Square'''


from models.rectangle import Rectangle


class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        for (i, arg) in enumerate(args):
            if i == 0:
                self.id = int(arg)
            elif i == 1:
                self.size = int(arg)
            elif i == 2:
                self.x = int(arg)
            elif i == 3:
                self.y = int(arg)
        if args is not None and len(args) == 0:
            for (k, v) in kwargs.items():
                if k == 'id':
                    self.id = int(v)
                elif k == 'size':
                    self.size = int(v)
                elif k == 'x':
                    self.x = int(v)
                elif k == 'y':
                    self.y = int(v)
 
