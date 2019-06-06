#!/usr/bin/python3
def read_file(filename=""):
    '''open a given file'''
    with open(filename, 'r') as f:
        print("{}".format(f.read()), end="")
