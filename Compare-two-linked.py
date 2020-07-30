#!/bin/python3

import os
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node


        self.tail = node

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(cur1, cur2):
    while (cur1 is not None and cur2 is not None):
        if cur1.data!=cur2.data:
            return 0
        cur1=cur1.next
        cur2=cur2.next
        if(cur1 is None and cur2 is not None) or(cur2 is None and cur1 is not None):
            return 0 
    return 1



if __name__ == '__main__':
