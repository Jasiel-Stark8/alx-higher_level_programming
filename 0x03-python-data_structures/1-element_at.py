#!/usr/bin/python3
def element_at(my_list, idx):
    for i in my_list[idx]:
        if i < 0:
            return None
        elif i > len(my_list):
            return None
        else:
            print(my_list[idx])
