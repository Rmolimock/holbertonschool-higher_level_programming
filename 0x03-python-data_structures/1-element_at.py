#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list):
        return None
    n = my_list[idx]
    if n < 1:
        return None
    else:
        return n
