#!/usr/bin/python3
"""Define a parent class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class that inherits from Base class and represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @width.setter
    def width(self, width):
        """Validate and set width"""
        if width is not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")

    @height.setter
    def height(self, height):
        """Validate and set height"""
        if height is not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("width must be > 0")

    @x.setter
    def x(self, x):
        if x <= 0:
            raise ValueError("x must be >= 0")

    @y.setter
    def y(self, y):
        if y <= 0:
            raise ValueError("y must be >= 0")

    @property
    def area(self):
        """Return the area of the rectangle"""
        return self.width * self.height
