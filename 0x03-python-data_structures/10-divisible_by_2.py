#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """finds all multiples of 2 in a list"""
    new_list = []

    IsMul = True
    NotMul = False
    for num in my_list:
        if num % 2 == 0:
            new_list.append(IsMul)
        else:
            new_list.append(NotMul)
    return (new_list)
