#!/usr/bin/python3
"""Say my name. Heisenberg"""


def say_my_name(first_name, last_name=""):
    """This function says the name of the user
    Args:
        @first_name: The first name
        @last_name: The last name"""
    if first_name is None:
        raise TypeError("first_name must be a string")
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
        return
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
        return
    print("My name is {} {}".format(first_name, last_name))
