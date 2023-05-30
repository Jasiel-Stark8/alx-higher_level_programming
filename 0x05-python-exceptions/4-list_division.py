#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
                new_list.append(result)
            except ZeroDivisionError:
                new_list.append(0)
                print("division by 0")
            except (TypeError):
                new_list.append(0)
                print("wrong type")
            except IndexError:
                new_list.append(0)
                print("out of range")
    finally:
        print(new_list)


# Test
list_1 = [10, 20, 30, 40]
list_2 = [2, 0, 5]
length = 5
result = list_division(list_1, list_2, length)
print(result)