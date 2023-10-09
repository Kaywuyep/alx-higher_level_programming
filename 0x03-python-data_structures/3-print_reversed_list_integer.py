#!/usr/bin/python3


'''function that prints all integers of a list, in reverse order'''


def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return
    for i in reversed(my_list):
        print('{:d}'.format(i))
