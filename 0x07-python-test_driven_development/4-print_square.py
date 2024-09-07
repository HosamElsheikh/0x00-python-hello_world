#!/usr/bin/python3
"""This prints a square"""


def print_square(size):
    """This is a function to print #s to form a square

    Args:
        size (int): The size of the square
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
        return
    if size < 0:
        raise ValueError("size must be >= 0")
        return
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
        return
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print("")
