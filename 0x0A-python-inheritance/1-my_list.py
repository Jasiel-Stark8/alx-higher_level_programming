#!/usr/bin/python3
"""Define a clsass MyList"""


class MyList(list):
    """
    A subclass of list that provides additional functionality for \
        printing the elements of the list in sorted order.
    """

    def print_sorted(self):
        """
        Prints the elements of the list in sorted (ascending) order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
