#!/usr/bin/python3
import sys

if __name__ == "__main__":
    arg_count = len(sys.argv) - 1  # Subtract 1 to not count the program name

    if arg_count == 0:
        print("0 arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))

    for i in range(arg_count):
        print("{}: {}".format(i, sys.argv[i]))
