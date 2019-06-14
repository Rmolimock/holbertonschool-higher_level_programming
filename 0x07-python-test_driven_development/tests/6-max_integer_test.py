#!/usr/bin/python3
'''This module contains one class, TestMaxInteger'''
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    '''Test cases for max_integer'''
    def test_normal(self):
        '''normal test case'''
        self.assertEqual(max_integer([1, 2, 3, 99, 4, 5]), 99)

    def test_max_at_end(self):
        '''test with max int at end of list'''
        self.assertEqual(max_integer([1, 2, 3, 4, 5, 99]), 99)

    def test_max_beginning(self):
        '''test with max int at beginning of list'''
        self.assertEqual(max_integer([99, 1, 2, 3, 4, 5]), 99)

    def test_none(self):
        '''test an empty list'''
        self.assertEqual(max_integer([]), None)

    def test_negative(self):
        '''test with a negative int'''
        self.assertEqual(max_integer([1, 2, 3, -4, 99, 5]), 99)

    def test_only_negative(self):
        '''test with all negative numbers'''
        self.assertEqual(max_integer([-1, -2, -99, -3, -4, -5]), -1)

    def test_one_element(self):
        '''test with one int in list'''
        self.assertEqual(max_integer([99]), 99)
