#!/usr/bin/python


def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    sort_keys = sorted(a_dictionary.keys())

    for key in sort_keys:
        print("{}: {}".format(key, a_dictionary[key]))

    return sort_keys
