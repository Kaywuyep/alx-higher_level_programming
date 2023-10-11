#!usr/bin/python3


def multiply_by_2(a_dictionary):
    """ returns a new dictionary with all values multiplied by 2"""
    return {key: value * 2 for key, value in a_dictionary.items()}


def print_sorted_dictionary(a_dictionary):
    sort_keys = sorted(a_dictionary.keys())
    for key in sort_keys:
        print("{}: {}".format(key, a_dictionary[key]))
