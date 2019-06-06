#!/usr/bin/python3
class BaseGeometry:
    '''this class has two methods that raise exceptions'''

    def area(self):
        '''raise exception message'''
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        '''make sure value is an int > 0'''
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
