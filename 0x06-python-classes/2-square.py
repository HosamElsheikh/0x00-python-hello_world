#!/usr/bin/python3
"""This class is to generate a square"""


class Square:
    """This class is to create a square"""
    def __init__(self, size=0):
        """Creates an instance of the class

        Arguments:
            @size: The size of the square. Defaults to 0.

        Raises:
            TypeError: Only integeres are accepted in size
            ValueError: size can't be a negative value
        """
        
        self.__size = size
        
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
