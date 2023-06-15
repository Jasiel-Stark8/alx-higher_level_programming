#!/usr/bin/python3
"""Define a module that writes an object to a text file
using json representation"""
import json


def save_to_json_file(my_obj, filename):
    """Save the object to a text file wuth JSON format"""
    with open(filename, 'w', encoding="UTF-8") as f:
        return json.dump(my_obj, f)
