#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    try:
        for i in range(len(my_list_1)):
            for j in range(len(my_list_2)):
                if i % j == 0:
                    return 0
                else:
                    new_list = my_list_1[i] / my_list_2[j]
        else:
            if len(my_list_1) < len(my_list_2):
                print("out of range")

    except ZeroDivisionError:
        print("division by 0")
        new_list = None

    except (TypeError, IndexError):
        new_list = None

    finally:
        print(new_list)
