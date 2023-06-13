#!/usr/bin/python3

def is_same_class(obj, a_class):
    """validate if object is an exact instance of specifeid class"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
