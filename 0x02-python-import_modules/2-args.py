#!/usr/bin/python3
import sys

if __name__ == '__main__':
    num = len(sys.argv) - 1
    # subtract 1 because the script name is also included in sys.argv
    if num == 1:
        print(f"{num} argument:")
    else:
        print(f"{num} arguments:")

    for i, arg in enumerate(sys.argv[1:], start=1):
        print(f"{i}: {arg}")
