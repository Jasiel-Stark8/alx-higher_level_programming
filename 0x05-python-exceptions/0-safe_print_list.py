#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    [print(x) for x in my_list]
    try:
        while (my_list != []):
            my_list = my_list[0:-1]
            x += 1
            return x
        # x can be bigger than len of my_list
    except:
        print("List is Empty")
    return my_list
