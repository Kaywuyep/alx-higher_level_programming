#!/usr/python3


'''function that finds all multiples of 2 in a list'''


def divisible_by_2(my_list=[]):
    if not my_list:
        return
    new = []
    isMultiple = True
    notMultiple = False
    for i in my_list:
        if i % 2 == 0:
            new.append(isMultiple)
        else:
            new.append(notMultiple)
    return new
