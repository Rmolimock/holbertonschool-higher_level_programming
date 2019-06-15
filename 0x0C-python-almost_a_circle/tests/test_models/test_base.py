#!/usr/bin/python3
'''This module contains three classes:
TestBase, TestRectangle, and TestSquare'''

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    '''unit tests for Base class'''

    def test_id(self):
        '''test that base id works in init method'''
        ob1 = Base()
        self.assertEqual(ob1.id, 1)

    def test_id_increment(self):
        ob2 = Base()
        self.assertEqual(ob2.id, 2)

    def test_declare_id(self):
        ob89 = Base(89)
        self.assertEqual(ob89.id, 89)

    def test_to_json_string_none(self):
        self.assertEqual(Base.to_json_string(None), '[]')

    def test_to_json_string_empty(self):
        self.assertEqual(Base.to_json_string([]), '[]')

    def test_to_json_string_dict(self):
        self.assertEqual(Base.to_json_string([{'id': 33}]), '[{"id": 33}]')

    def test_to_json_string_type(self):
        self.assertEqual(type(Base.to_json_string([ { 'id': 12 }])), str)

    def test_from_json_string_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        self.assertEqual(Base.from_json_string('[]'), [])

    def test_from_json_string_normal(self):
        self.assertEqual(Base.from_json_string('[{ "id": 89 }]'), [{'id': 89}])

    def test_from_json_string_type(self):
        self.assertEqual(type(Base.from_json_string('[{ "id": 89 }]')), list)

class TestRectangle(unittest.TestCase):
    '''unit tests for Rectangle class'''

    def test_rectangle_width(self):
        ob1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(ob1.width, 1)

    def test_rectangle_height(self):
        ob1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(ob1.height, 2)

    def test_rectangle_x(self):
        ob1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(ob1.x, 3)

    def test_rectangle_y(self):
        ob1 = Rectangle(1, 2, 3, 4)
        self.assertEqual(ob1.y, 4)

