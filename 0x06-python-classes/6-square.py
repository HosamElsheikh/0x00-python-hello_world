#!/usr/bin/python3

"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
            position (coordinates): The position of the square
        """

        self.size = size
        self.position = position

    def area(self):
        """Returns the area of the square at hand"""
        return self.__size * self.__size

    @property
    def size(self):
        """This function returns the value of the size"""
        return self.__size

    @property
    def position(self):
        """This function returns the position of the square in a plain"""

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

    @position.setter
    def position(self, value):
        """This function sets the current position of the square

        Args:
            value (tuple): The coordinates of the square
        """
        if not isinstance(value, tuple) or len(value) != 2 or \
           not isinstance(value[0], int) or not isinstance(value[1], int) or \
           value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """This function results in printing the square"""
        if self.__size == 0:
            print("")

        for lines in range(self.__position[1]):
            print("")

        for i in range(self.__size):
            for j in range(self.__size):
                if j == 0:
                    for spaces in range(self.__position[0]):
                        print(" ", end="")
                print("#", end="")
            print("")
