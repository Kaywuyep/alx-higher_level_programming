#!/usr/bin/python3
numbers = [i for i in range(0, 100)]
for i in numbers:
    print(f"{i:02d}", end=', ')
print()  # This adds a new line after printing all elements
