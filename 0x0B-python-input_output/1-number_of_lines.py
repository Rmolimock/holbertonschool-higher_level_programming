#!/usr/bin/python3
def number_of_lines(filename=""):
    '''find the number of lines in a txt file'''
    with open(filename, 'r') as f:
        return len(f.readlines())
