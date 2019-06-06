#!/usr/bin/python3
def append_write(filename="", text=""):
    '''append a file with text'''
    with open(filename, mode="a", encoding="utf-8") as f:
        return f.write(text)
