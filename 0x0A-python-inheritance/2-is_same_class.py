#!/usr/bin/python3
"""an inheritance module"""


def is_same_class(obj, a_class):
    """
    function that returns True if the object is exactly an instance
    of the specified class ; otherwise False

    param: obj- object
           a_class - the class defined
    """
    return type(obj) is a_class
