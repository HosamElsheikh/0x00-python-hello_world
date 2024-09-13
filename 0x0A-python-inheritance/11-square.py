#!/usr/bin/python3
"""This is a square module"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """This is the square class that we will impelement"""
    def __init__(self, size):
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
