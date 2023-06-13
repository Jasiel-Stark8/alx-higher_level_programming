#!/usr/bin/python3
"""Define a clsass MyList"""


class MyList(list):
    """Return sorted list in ascending order"""
    def print_sorted(self):
        return self.sort()
