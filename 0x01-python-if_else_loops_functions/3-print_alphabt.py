#!/usr/bin/python3
alpha = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in 'qe']
for char in alpha:
    print(char, end='')
