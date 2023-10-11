#!/usr/bin/python3


def only_diff_elements(set_1, set_2):
    """set of all elements present in only one set"""
    uncommon_elmt = set_1.symmetric_difference(set_2)

    return uncommon_elmt
