#!/usr/bin/python3


def search_replace(my_list, search, replace):
    """Replaces all occurrences of an element by another in a new list."""
    new_list = replace_elements(my_list, search, replace)
    return new_list


def replace_elements(new_list, search, replace):
    """Replaces all occurrences of an element in a list."""
    return [replace if element == search else element for element in new_list]
