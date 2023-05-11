#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
abs_val = abs(number)
if number != None:
    if abs_val % 10 > 5:
        print(f"Last digit of {number} is {abs_val % 10} and is greater than 5\n")
        if abs_val % 10 == 0:
            print(f"Last digit of {number} is {abs_val % 10} and is 0\n")
    else:
        print(f"Last digit of {number} is {abs_val % 10} and is less than 6 and not 0\n")
