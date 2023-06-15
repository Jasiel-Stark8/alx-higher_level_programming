#!/usr/bin/python3
"""Define a module that writes to a file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of
    characters written.
    """
    try:
        with open(filename, 'w', encoding="UTF-8") as file:
            file.write(text)
            return len(text)
    except OSError:
        return -1  # Returns -1 when an error occurs
