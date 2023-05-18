#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    for i in len(range(my_list)):
        result += set(my_list)
    return result
