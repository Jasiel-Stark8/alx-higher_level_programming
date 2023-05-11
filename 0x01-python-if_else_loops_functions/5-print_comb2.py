#!/usr/bin/python3
numbers = range(0, 100)
for i in numbers:
    if i == 99:
        print(f"{i:02d}", end="\n")
    else:
        print(f"{i:02d}, ", end="")