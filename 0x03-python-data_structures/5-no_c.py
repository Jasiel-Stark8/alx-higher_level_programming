#!/usr/bin/python3
def no_c(my_string):
    string = ""
    for char in my_string.split():
        if char != 'c' and char != 'C':
            string += char
        print(string)
