#!/usr/bin/python3
hexa = [i for i in range(0, 99)]
print('\n'.join(f"{i} = 0x{i:02x}" for i in hexa))
