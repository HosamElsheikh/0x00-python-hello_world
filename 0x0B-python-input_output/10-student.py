#!/usr/bin/python3
"""This is a module used for a student"""


class Student:
    """A class of Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method gets specific attributes from the class"""
        if attrs is not None:
            for i in attrs:
                return self.__dict__[i]
        return self.__dict__
