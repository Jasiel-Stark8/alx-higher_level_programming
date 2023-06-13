#!/usr/bin/python3
"""Defnie a base class BaseGeometry"""


class BaseGeometry:
    """ Initialize BaseGeometry"""

    def area(self):
        """Raise an exception if the area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")
