#!/usr/bin/python3
"""an inheritance module"""


def inherits_from(obj, a_class):
    """
    function that returns True if the object is an instance
    of a class that inherited (directly or indirectly)
    from the specified class ; otherwise False.


    param: obj - object
           a_class - class
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
