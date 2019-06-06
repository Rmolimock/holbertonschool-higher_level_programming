#!/usr/bin/python3
def read_lines(filename="", nb_lines=0):
    '''reads file up to the nb_lines number of lines'''
    with open(filename, encoding="utf-8") as f:
        count = 0
        for line in f:
            count += 1
            if count <= nb_lines or nb_lines <= 0:
                print(line, end="")
