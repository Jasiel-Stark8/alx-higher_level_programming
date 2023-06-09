#!/usr/bin/python3
"""Module 0-add_integer"""


def add_integer(a, b=98):
    """Add integer"""
    if a is not isinstance(b, int):
        raise TypeError("a must be an integer")
    if b is not isinstance(b, int):
        raise TypeError("b must be an integer")
    type(int(a))
    type(int(b))
    return a + b
