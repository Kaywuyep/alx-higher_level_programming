#!/usr/bin/python3
"""a simple python class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary representation of a simple data structure"""
    return obj.__dict__