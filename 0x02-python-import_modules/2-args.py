#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv) - 1
    argv = sys.argv
    if argc is 0:
        print("{} arguments.".format(argc))
    elif argc is 1:
        print("{} argument:".format(argc))
    elif argc > 1:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, argv[i + 1]))
