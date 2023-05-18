#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    return a_dictionary.keys(), [key * 2 for key in a_dictionary.values()]
# print(multiply_by_2({1: 2, 2: 4, 3: 6}))
