#!/usr/bin/python3
import sys
import calculator_1

if len(sys.argv) - 1 != 3:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    sys.exit(1)

operator = sys.argv[2]
if operator not in calculator_1.operator:
    print("Unknown operator. Available operators: +, -, * and /")
    sys.exit(1)

a = int(sys.argv[1])
b = int(sys.argv[3])
result = calculator_1.operator[operator](a, b)

print("{} {} {} = {}".format(a, operator, b, result))
