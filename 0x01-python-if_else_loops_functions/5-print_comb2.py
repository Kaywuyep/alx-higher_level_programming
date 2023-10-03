#!/usr/bin/python3
numbers = [i for i in range(0, 100)]
print(', '.join(f"{i:02d}" for i in numbers), end='\n')
