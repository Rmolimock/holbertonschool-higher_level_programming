#!/usr/bin/python3
class MyList(list):
    '''print sorted elements of self'''
    def print_sorted(self):
        print(sorted(self))
