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

    @property
    def width(self):
        """Get width"""
        return self.__width

    @width.setter
    def width(self, width):
        """Validate and set width"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = width

    @property
    def height(self):
        """Get height"""
        return self.__height

    @height.setter
    def height(self, height):
        """Validate and set height"""
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height <= 0:
            raise ValueError("height must be > 0")
        self.__height = height

    @property
    def x(self):
        """Get x-coordinate"""
        return self.__x

    @x.setter
    def x(self, x):
        """Validate and set x-coordinate"""
        if not isinstance(x, int):
            raise TypeError("x must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        self.__x = x

    @property
    def y(self):
        """Get y-coordinate"""
        return self.__y

    @y.setter
    def y(self, y):
        """Validate and set y-coordinate"""
        if not isinstance(y, int):
            raise TypeError("y must be an integer")
        if y < 0:
            raise ValueError("y must be >= 0")
        self.__y = y

    def display(self):
        """Print Rectangle with the '#' character"""
        print("\n" * self.y, end="")
        for i in range(self.height):
            print(" " * self.x, end="")
            print("#" * self.width)

    def __str__(self):
        """Print string representation of Rectangle"""
        return f"[Reectangle] ({self.id}) {self.x}/{self.y} \
            - {self.width}/{self.height}"
