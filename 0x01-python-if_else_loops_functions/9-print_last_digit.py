#!/usr/bin/python3
def print_last_digit(number):
    last_digit = abs(number) % 10  # calculate the last digit
    print(last_digit, end='')  # print the last digit without newline
    return last_digit  # return the last digit
