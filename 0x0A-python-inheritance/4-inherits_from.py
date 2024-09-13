#!/usr/bin/python3
"""Docstring for the class"""


def inherits_from(obj, a_class):
    """This implements the functionality.
    Args:
        @obj: This is the object we are checking
        @a_class: This checks the class
        """
    return issubclass(type(obj), a_class) and not type(obj) is a_class
