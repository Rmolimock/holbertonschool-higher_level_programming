#!/usr/bin/python3
for i in range(9):
    for k in range(i + 1, 10):
        if k > 1 and k <= 46:
            print(', ', end="")
        print('{:d}{:d}'.format(i, k), end="")
print()
