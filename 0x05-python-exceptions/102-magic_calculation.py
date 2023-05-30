#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(0, 103):
        try:
            if i < a:
                result += a
        except IndexError:
            result += b
        result = a + b
    return result
