#!/usr/bin/python3
"""square class main"""


class Square():
    """square class"""

    def __init__(self, size=0):
        """ Instance of class Square
    Args:
        @size (int): size of side of square
        """
        if not isinstance(int, size):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
