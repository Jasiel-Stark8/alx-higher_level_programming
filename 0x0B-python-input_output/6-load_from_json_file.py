#!/usr/bin/python3
"""Module to load from json file"""
import json


def load_from_json_file(filename):
    """Create object from JSON"""
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.dump(filename, f)
