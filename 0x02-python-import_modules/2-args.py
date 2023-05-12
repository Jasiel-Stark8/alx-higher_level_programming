#!/usr/bin/python3

if __name__ == '__main__':
    import sys
    num = len(sys.argv) - 1
    # subtract 1 because the script name is also included in sys.argv

    if num == 0:
        print("0 arguments.")
    elif num == 1:
        print("{} argument:".format(num))
    else:
        print("{} arguments:".format(num))

    for i, arg in enumerate(sys.argv[1:], start=1):
        print("{}: {}".format(i, arg))
