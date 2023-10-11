#!/usr/bin/python3


def simple_delete(a_dictionary, key=""):
    """ deletes a key in a dictionary"""
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary


def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())
    for key in sort_keys:
        print("{}: {}".format(key, a_dictionary[key]))
