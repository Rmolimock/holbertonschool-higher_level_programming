#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return None
    new = []
    for i in my_list:
        new.append(False) if i % 2 else new.append(True)
    return new
