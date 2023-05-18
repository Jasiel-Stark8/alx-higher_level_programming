#!/usr/bin/python3
def uniq_add(my_list=[]):
    result = 0
    my_list = set(my_list)
    for i in my_list:
        result += i
    return result
# if __name__ == "__main__":
#     print(uniq_add([1, 2, 1, 4, 3, 3, 5, 5, 1, 7, 8]))
