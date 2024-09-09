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

    def area(self):
        """This one returns the area of the rectangle"""
        return self.__height * self.__width

    def perimeter(self):
        """This one returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height + self.__width) * 2

    def __str__(self):
        """This is used when printing an instance of the class"""
        str = ""
        if self.__width == 0 or self.__height == 0:
            return str
        for i in range(self.__height):
            for j in range(self.__width):
                str += "#"
            if i == self.__height - 1:
                break
            str += "\n"
        return str
