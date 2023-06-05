#!/usr/bin/python3
"""Class that instanciates a Linked List"""


class Node:
    def __init__(self, data):
        """Function that instanciates a node"""
        self.data = data
        self.next = None


class LinkedList():
    def __init__(self):
        """Function that instanciates a Linked List"""
        self.head = None

    def insert(self, data, position):
        """Function that inserts a node"""
        if self.head is None:
            node1 = Node(data)
        if position == 0:
            node1.next = self.head
            self.head = node1
        else:
            curr_node = self.head
            for i in range(position - 1):
                curr_node = curr_node.next
            node1.next = curr_node.next
            curr_node.next = node1
