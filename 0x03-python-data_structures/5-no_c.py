#!/usr/bin/python3
def no_c(my_string):
    for i in my_string.split():
        if i == 'c' and i == 'C':
            return i.strip()
        print(my_string)
