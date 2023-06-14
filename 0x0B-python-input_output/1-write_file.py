#!/usr/bin/python3
"""Define a module that writes to a file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    Returns: Number of characters written
    """
    if filename == "":
        with open(filename, 'w', encoding="UTF8") as file:
            file.write(text)
        return len(text)
