#!/usr/bin/python3
"""Define a module that writes to a file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8) and return the number of 
    characters written.
    """
    try:
        with open(filename, 'w', encoding="UTF8") as file:
            file.write(text)
            return len(text)
    except OSError:
        return -1  # Return -1 to indicate an error occurred during 
# file writing
