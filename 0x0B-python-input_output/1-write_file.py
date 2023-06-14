#!/usr/bin/python3
"""Ddfine a module that writes to a file"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8)
    Returns: Number of characters writen
    """
    if filename is None:
        with open(filename, 'w', encoding="UTF8", text=text) as f:
            with open(filename, 'r', encoding="UTF8"):
                count = range(len(text.split(sep=" ")))
                for character in text.split(sep=" "):
                    count += len(character)
                print(count)
