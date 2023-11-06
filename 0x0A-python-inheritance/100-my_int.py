#!/usr/bin/python3
"""a simple module"""


class MyInt(int):
    """a class MyInt that inherits from int"""

    def __eq__(self, other):
        """Override the == operator."""
        # return self.real != other
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator."""
        # return self.real == other
        return super().__eq__(other)
