#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
val = abs(number)
message = f"Last digit of {number} is {val % 10} "
if val % 10 > 5:
    print(f"{message} and is greater than 5\n")
    if val % 10 == 0:
        print(f"{message} and is 0\n")
else:
    print(f"{message} and is less than 6 and not 0\n")
