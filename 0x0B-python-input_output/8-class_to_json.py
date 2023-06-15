#!/usr/bin/python3
"""A module that returns the dictionary description with simple
data structure (list, dictionary, string, integer and boolean)
for JSON serialization of an object:
"""
import json


def class_to_json(obj):
    """
    Returns a dictionary description of an object's attributes
    with simple data structures suitable for JSON serialization.
    """
    if isinstance(obj, (list, dict, str, int, bool)):
        return obj

    result = {}
    for attr in obj.__dict__:
        value = obj.__dict__[attr]
        if isinstance(value, (list, dict, str, int, bool)):
            result[attr] = value

    return result

