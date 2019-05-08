#!/usr/bin/python3
def element_at(my_list, idx):
    if idx > len(my_list) or my_list[idx] < 0 or not my_list[idx]:
        return None
    else:
        return my_list[idx]
