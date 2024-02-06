#!/usr/bin/python3
"""This is a square class"""


class Square:
    """This creates a square empty class"""
    def __init__(self, size=None):
        self.__size = size
        if (type(size) != int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
