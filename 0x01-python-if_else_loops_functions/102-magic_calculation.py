#!/usr/bin/python3
# import dis
def magic_calculation(a, b, c):
    if a < b:
        return c
    elif c > b:
        return a + b
    return a * b - c


# print(magic_calculation(1, 2, 3))
# dis.dis(magic_calculation)