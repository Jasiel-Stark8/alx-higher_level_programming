#!/usr/bin/python3
"""Defnie an empty class BaseGeometry"""


class BaseGeometry:
    """ Initialize BaseGeometry"""

    def area(self):
        """Raise an exception if the area is not implemented"""
        raise NotImplementedError("area() is not implemented")
