#!/usr/bin/python3
"""Module 0-add_integer"""


def add_integer(a, b=98):
    """This module adds 2 integers and returns the sum \
        which is casted in an int()"""

    if a is not isinstance(a, int):
        raise TypeError("a must be an integer")
    if b is not isinstance(b, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
