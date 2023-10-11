#!/usr/bin/python3


def uniq_add(my_list=[]):
    """adds all unique integers in a list (only once for each integer)"""
    # covert integers to se to avoid duplicate
    uniq_set = set(my_list)
    result = sum(uniq_set)
    return result
