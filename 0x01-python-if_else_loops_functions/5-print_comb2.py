#!/usr/bin/python3
for i in range(0, 100):
    if i > 0:
        print(", {:02d}".format(i), end="")
    else:
        print("{:02d}".format(i), end="")
print('')
