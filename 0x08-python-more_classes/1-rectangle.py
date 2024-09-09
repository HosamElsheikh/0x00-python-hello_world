#!/usr/bin/python3
"""This creates a python class"""


class Rectangle:
    """This is a rectangle class"""
    def __init__(self, width=0, height=0):
        """Initializes a new rectangle class.
        Ars:
            @width (int): The width of the triangle
            @height(int): The height of the triangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
