#!/usr/bin/python3
"""Module 0-add_integer"""


def add_integer(a, b=98):
    """This module adds 2 integers and returns the sum \
        which is casted in an int()"""

    if a is not isinstance(a, int) and a is not isinstance(a, float):
        raise TypeError("a must be an integer or a float")
    if b is not isinstance(b, int) and a is not isinstance(a, float):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)


print(add_integer(1))
