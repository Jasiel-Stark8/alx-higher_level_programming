#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= my_list.size():
        print(my_list)
    else:
        my_list.insert(idx, element)
        print(my_list)
