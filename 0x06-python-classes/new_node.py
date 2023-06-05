#!/usr/bin/python3
"""Node class"""


class Node():
    def __init__(self, data):
        self.data = None

class LinkedList():
    def __init__(self):
        self.head = None

    def print_list(self):
        if self.head is None:
            print("Linked List is empty... Nothing to print")
        else:
            current = self.head
            print(current.data)
        while current.next is not None:
            current = current.next
            print(current.data)