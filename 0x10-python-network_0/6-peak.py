#!/usr/bin/python3
"""this module finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """return peak of the list"""
    if not list_of_integers:
        return None

    low, high = 0, len(list_of_integers) - 1

    while low < high:
        mid = (low + high) // 2

        if list_of_integers[mid] > list_of_integers[mid + 1]:
            # Peak is on the left side
            high = mid
        else:
            # Peak is on the right side (or mid itself)
            low = mid + 1

    return list_of_integers[low]
