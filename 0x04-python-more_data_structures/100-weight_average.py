#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    for i in my_list:
        return sum(my_list) / len(my_list)
