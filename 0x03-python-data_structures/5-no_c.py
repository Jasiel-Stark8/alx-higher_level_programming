#!/usr/bin/python3
def no_c(my_string):
    for i in my_string.split():
        if i is 'c' and i is 'C':
            return i.strip()
        print(my_string)
