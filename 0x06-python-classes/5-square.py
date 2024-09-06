#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """

        self.size = size

    def area(self):
        """Returns the area of the square at hand"""
        return self.__size * self.__size

    @property
    def size(self):
        """This function returns the value of the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """This function sets a size for the given square

        Args:
            value (int): The length of any of the square sides
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """This function results in printing the square"""
        if self.__size == 0:
            print("")
        for i in range(self.__size):
            for j in range(self.__size):
                print("#", end="")
            print("")
