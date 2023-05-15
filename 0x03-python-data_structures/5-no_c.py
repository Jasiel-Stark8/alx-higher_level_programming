#!/usr/bin/python3
def no_c(my_string):
    for i in my_string.split():
        return i.strip('c' and 'C')
    print(my_string)
