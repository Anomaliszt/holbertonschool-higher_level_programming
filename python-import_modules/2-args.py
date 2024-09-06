#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argc = len(sys.argv) - 1

    if argc == 0:
        print("0 arguments.")
    elif argc == 1:
        print("1 argument:")
    else:
        print("{:d} arguments:".format(argc))

    for i, arg in enumerate(sys.argv[1:], 1):
        print("{:d}: {:s}".format(i, arg))
