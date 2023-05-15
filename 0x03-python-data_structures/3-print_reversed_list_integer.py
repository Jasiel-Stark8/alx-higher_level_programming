# def print_reversed_list_integer(my_list=[]):
#     for i in my_list[::-1]:
#         print("{:d}".format(i))


def print_reversed_list_integer(my_list=[]):
    print("{:d}".format(i) for i in my_list.reverse())
