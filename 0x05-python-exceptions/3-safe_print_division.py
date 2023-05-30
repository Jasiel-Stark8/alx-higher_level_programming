#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        print("Can't Divide By Zero.")
        return None
    finally:
        print("Inside result: {}".format(result))

    return result
