#!/usr/bin/python3
"""Define a clsass MyList"""


class MyList(list):
    """Define class the returns list in ascending order"""
    def print_sorted(self):
        """prints the list in ascending order"""
        sorted_list = sorted(self)
        print(sorted_list)
