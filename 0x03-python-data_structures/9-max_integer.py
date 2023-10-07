#!/usr/bin/python3


'''function that finds the biggest integer of a list.'''


def max_integer(my_list=[]):
    length = len(my_list)
    if length == 0:
        return None
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
