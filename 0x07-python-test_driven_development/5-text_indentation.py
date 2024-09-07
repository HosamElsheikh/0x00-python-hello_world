#!/usr/bin/python3
"""This function prints two lines after the period
comma, or question mark
"""


def text_indentation(text):
    """This function adds an extra line.
    Args:
        @text: The text
    """
    skip_space = False
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for i in text:
        if skip_space is True and i == " ":
            skip_space = False
            continue
        elif i in ".?:":
            print(i)
            print("")
            skip_space = True
        else:
            print(i, end="")
