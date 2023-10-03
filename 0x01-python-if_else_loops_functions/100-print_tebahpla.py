#!/usr/bin/python3
for i in range(122, 96, -1):
    alternate = i if i % 2 == 0 else i - 32
    print("{:c}".format(alternate), end='')
