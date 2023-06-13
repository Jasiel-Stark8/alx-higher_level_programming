#!/usr/bin/python3
"""Define a clsass MyList"""


class MyList(list):
    """Define class the returns list in ascending order"""
    def print_sorted(self):
        """Prints sorted list"""
        print(sorted(self))
