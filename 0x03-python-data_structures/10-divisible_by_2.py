#!/usr/python3


def divisible_by_2(my_list=[]):
    '''function that finds all multiples of 2 in a list'''
    new = []

    isMultiple = True
    notMultiple = False
    for num in my_list:
        if num % 2 == 0:
            new.append(isMultiple)
        else:
            new.append(notMultiple)
    return new
