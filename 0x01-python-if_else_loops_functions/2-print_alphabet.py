#!/usr/bin/python3
alpha = [chr(i) for i in range(ord('a'), ord('z')+1)]
for char in alpha:
    print('{:c}'.format(ord(char)), end='')
