#!/usr/bin/python3
"""Define a parent class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """Class that inherites a class Base and represents a Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize Rectangle"""
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        super.__init__(id)