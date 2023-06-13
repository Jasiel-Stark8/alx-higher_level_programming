#!/usr/bin/python3
"""A module that defines a class Square that inherits from Rectangle"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represent Square class"""

    def __init__(self, size):
        """Initialize a new Square"""
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        """Return square area"""
        return self.__size * self.__size
