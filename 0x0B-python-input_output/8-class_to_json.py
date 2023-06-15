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
    return obj.__dict__
