#!/usr/bin/python3
""""Defining a function that returns the list of available attributes and methods of an object"""


def lookup(obj):
    """Returns list of attributes of the object"""
    return dir(obj)
