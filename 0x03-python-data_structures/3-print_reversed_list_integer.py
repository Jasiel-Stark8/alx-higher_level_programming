# def print_reversed_list_integer(my_list=[]):
#     for i in my_list[::-1]:
#         print("{:d}".format(i))


def print_reversed_list_integer(my_list=[]):
    my_list.reverse()
    for i in my_list:
        if not isinstance(i, int):
            print("{:d}".format(i))
        else:
            print(i)
