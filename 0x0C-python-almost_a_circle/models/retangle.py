#!/usr/bin/python3
"""Define a parent class Rectangle"""
from models.base import Base
Base = __import__('').Base


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

    def update(self, *args):
        """Update Rectangle"""
        # handle if none is given
        if len(args) <= 1:
            raise ValueError("Coordinates can't be empty")

        # if only x is given
        if len(args) == 2:
            if not isinstance(args[1], int):
                raise TypeError("First argument must be an \
                    integer representing 'x'")
            if args[1] < 0:
                raise ValueError("'x' must be >= 0")
            self.__x = args[1]
            return

        # if x and y are given
        if len(args) == 3:
            if not isinstance(args[1], int):
                raise TypeError("First argument must be an \
                    integer representing 'x'")
            if args[1] < 0:
                raise ValueError("'x' must be >= 0")
            self.__x = args[1]

            if not isinstance(args[2], int):
                raise TypeError("Second argument must be an \
                    integer representing 'y'")
            if args[2] < 0:
                raise ValueError("'y' must be >= 0")
            self.__y = args[2]
            return

        # handle when more than 3 arguments (filename inclusive) are given
        if len(args) > 3:
            raise ValueError("Too many arguments provided, \
                maximum of 2 (x, y) are allowed")
        