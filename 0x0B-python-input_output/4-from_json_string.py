#!/usr/bin/python3
"""Defines a module that returns an object represented by a json string"""
import json


def from_json_string(my_str):
    """returns object as a JSON string"""
    return json.loads(my_str)
