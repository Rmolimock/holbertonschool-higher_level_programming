#!/usr/bin/python3
def uppercase(str):
    for c in str:
        num = ord(c)
        if num >= 97 and num <= 122:
            num -= 32
        print("{:c}".format(num), end='')
    print()
