#!/usr/bin/python3
"""an inheritance module"""


def lookup(obj):
    """
    function that returns the list of available attributes
    and methods of an object
    param: obj - the object
    """
    return dir(obj)
