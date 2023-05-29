#!/usr/bin/python3
try:
    num = int(input("Enter a number: "))
except:
    print("Enter only digits not words... ")
else:
    print(num)
finally:
    print("Nothing Found. Exiting now... Done")
