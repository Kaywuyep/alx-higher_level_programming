#!/usr/bin/python3
"""a simple module defines a class Student"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initializes a student with first_name, last_name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance."""
        dic = {}
        if attrs is None:
            return self.__dict__
        for i in attrs:
            if hasattr(self, i):
                dic[i] = getattr(self, i)
        return dic
