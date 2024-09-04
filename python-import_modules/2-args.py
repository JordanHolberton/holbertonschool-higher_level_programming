#!/usr/bin/python3

if __name__ == "__main__":

    import sys
    argv = sys.argv
    argc = len(argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("{} argument:".format(argc, end=""))
    else:
        print("{} arguments:".format(argc))
    for i in range(argc):
        print("{}: {}".format(i + 1, sys.argv[i+1]))
