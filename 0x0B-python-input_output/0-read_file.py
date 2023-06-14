#!/usr/bin/python3

def read_file(filename=""):
    """Read from file (UTF encoding) and print to stdout"""
    with open(filename, 'r', encoding="utf") as txt:
        print(txt.read(), end='')
