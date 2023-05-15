#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    print(my_list)
    # print(my_list[::-1])


if __name__ == '__main__':
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print_reversed_list_integer(my_list)
