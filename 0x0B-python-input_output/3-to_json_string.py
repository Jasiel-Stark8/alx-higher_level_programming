#!/usr/bin/python3
"""Define a modile that returns the JSON representation of an object(string)"""
import json


def to_json_string(my_obj):
    """Convert object(string) to JSON"""
    return json.dumps(my_obj)
