#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for i in range(0, list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            result = None
        except TypeError:
            print("wrong type")
            result = None
        except IndexError:
            print("out of range")
            result = None
        finally:
            new_list.append(result)
    return new_list
