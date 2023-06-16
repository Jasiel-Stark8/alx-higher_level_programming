#!/usr/bin/python3
"""Defines a parent class Base"""


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a Base object"""
        self.id = id
        if self.id is not None:
            self.id = id
        Base.__nb_objects += 1
