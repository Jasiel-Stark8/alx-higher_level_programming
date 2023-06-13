#!/usr/bin/python3

def is_same_class(obj, a_class):
    """validate if object is an exact instance of specifeid class

    Args: (obj) is the object to be validated
    is matched against an exact class name

    Returns:
    True if obj is an exact instance of a_class
    False otherwise
    """

    if type(obj) == a_class:
        return True
    return False
