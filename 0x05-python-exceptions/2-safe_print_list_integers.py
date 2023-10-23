#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """prints the first x elements of a list and only integers"""
    count = 0
    try:
        for i in range(x):
            value = my_list[i]
            if isinstance(value, int):
                print("{:d}".format(value), end="")
                count += 1
        print()
        return count
    except IndexError:
        print()
        return count
