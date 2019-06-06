#!/usr/bin/python3
def write_file(filename="", text=""):
    '''write text into a file'''
    with open(filename, mode="w+", encoding="utf-8") as f:
        return f.write(text)
