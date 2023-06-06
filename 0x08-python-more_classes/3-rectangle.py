#!/usr/bin/python3
"""Define a class Rectangle"""


class Rectangle:
    """An empty class Rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """Return the width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return the perimiter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return (self.width + self.height) * 2

    def print(self):
        """Print the rectangle str("#")"""
        if self.width == 0 or self.height == 0:
            print()
        else:
            for i in range(self.height):
                for j in range(self.width):
                    print("#", end="")
                print()
