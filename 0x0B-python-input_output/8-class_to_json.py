#!/usr/bin/python3
"""A module that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """
    Returns dictionary description of python Data structures
    (list, dictionary, string, integer and boolean)
    """
    if isinstance(obj, (list, dict, str, int, bool)):
        return (obj)
    elif hasattr(obj, '__dict__'):
        return obj.__dict__
    else:
        raise TypeError("Object type is not supported: " + type(obj).__name__)
