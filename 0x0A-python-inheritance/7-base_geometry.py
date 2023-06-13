#!/usr/bin/python3
"""Defnie a base class BaseGeometry"""


class BaseGeometry:
    """BaseGeometry class"""

    def area(self):
        """Raises an exception if the area is not implemented"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates the value as an integer"""
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")

