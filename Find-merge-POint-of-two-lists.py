#!/bin/python3

import math
import os
import random
import re
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

#
def findMergeNode(head1, head2):
    if head1==head2:
        return head1.data
    else:
        while head2 is not None:
            x=head1
            while x is not None:
                if x==head2:
                    return head2.data
                x=x.next
            head2=head2.next
    return 0

if __name__ == '__main__':
