#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    i = 0
    while 1:
        try:
            while i < x:
                print(my_list[i], end="")
                i += 1
            print()
            break
        except IndexError:
            print()
            break
    return i
