#!/usr/bin/python3
"""a module that saya a name"""


def say_my_name(first_name, last_name=""):
    """
    Prints the message "My name is <first name> <last name>".

    :param first_name: First name (must be a string).
    :param last_name: Last name (default is an empty string).
    :return: None
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
