#!/usr/bin/python3
def magic_calculation(a, b):
    result = 0
    for i in range(0, 103):
        try:
            if i < a:
                result += i
            if i > b:
                result += b[i]
        except IndexError:
            break
        result = a + b
    return result
