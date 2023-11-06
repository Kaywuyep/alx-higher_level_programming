#!/usr/bin/python3
"""an inheritance module"""


def is_kind_of_class(obj, a_class):
    """
    function that returns True if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class ; otherwise False

    param: obj - object
           a_class - a class
    """
    return isinstance(obj, a_class)
