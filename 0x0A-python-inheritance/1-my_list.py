#!/usr/bin/python3
"""an inheritance module"""


class MyList(list):
    """class MyList that inherits from list"""
    def print_sorted(self):
        """Prints the sorted list in ascending order."""
        print(sorted(self))
