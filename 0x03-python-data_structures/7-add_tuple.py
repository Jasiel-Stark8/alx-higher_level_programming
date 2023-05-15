#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_c = tuple_a() and tuple_b()
    for i in tuple_a:
        for j in tuple_b:
            print(i[0] + j[0] and i[1] + j[1])
    return tuple_c
