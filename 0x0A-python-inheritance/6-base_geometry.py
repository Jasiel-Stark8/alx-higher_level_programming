#!/usr/bin/python3
"""Defnie a base class BaseGeometry"""


class BaseGeometry:
    """ Initialize BaseGeometry"""

    def area(self):
        """Raise an exception if the area is not implemented"""
        raise Exception("area() is not implemented")
