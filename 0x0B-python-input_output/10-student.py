#!/usr/bin/python3
"""This is a module used for a student"""


class Student:
    """A class of Student"""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """This method gets specific attributes from the class I cheated it"""
        if type(attrs) is list and \
                all(type(ele) is str for ele in attrs):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__
