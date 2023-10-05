#!/usr/bin/python3
if __name__ == "__main__":
    '''a program that prints the result of the addition of all arguments'''
    from sys import argv
    args = argv[1:]
    result = sum(map(int, args))
    print(result)
