#!/usr/bin/python3
"""This creates a python class"""


class Rectangle:
    """This is a rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes a new rectangle class.
        Ars:
            @width (int): The width of the triangle
            @height(int): The height of the triangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

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
        rectangle_str = ""
        if self.__width == 0 or self.__height == 0:
            return rectangle_str
        for i in range(self.__height):
            rectangle_str += (str(self.print_symbol)) * self.__width
            if i != self.__height - 1:
                rectangle_str += "\n"
        return rectangle_str

    def __repr__(self):
        """This is a special method for the code to create the string"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """This is called to delete an instance of the class"""
        print("Bye rectangle...")
        type(self).number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_1.area() < rect_2.area():
            return rect_2
        else:
            return rect_1
