#!usr/bin/python3


'''a function that retrieves an element from a list like in C.'''


def element_at(my_list, idx):
    if idx < 0:
        return None
    list_len = len(my_list) - 1
    if idx > list_len:
        return None
    for i, num in enumerate(my_list):
        if i == idx:
            return num
