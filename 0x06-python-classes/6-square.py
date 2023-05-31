#!/usr/bin/python3
"""Define a Class Square"""


class Square:
    """Class defining Square"""
    def __init__(self, size=0, position=(0, 0)):
        # Initialize the private attributes
        self.__size = size  # Initialize size attribute
        self.__position = position  # Initialize position attribute

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        # Validate and set the size attribute
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        # Validate and set the position attribute
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(x, int) for x in value) or any(x < 0 for x in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        # Calculate and return the area of the square
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            # If size is 0, print an empty line
            print("")
        else:
            for i in range(self.__position[1]):
                # Print empty lines based on the y-position
                print()
            for i in range(self.__size):
                # Print the square with the specified position
                print(" " * self.__position[0], end="")
                for j in range(self.__size):
                    print("#", end="")
                print()
