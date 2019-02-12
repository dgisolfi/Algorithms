#!/usr/bin/env python3
# 2019-1-22

import sys
sys.path.append('..')
from assign_1.DataStructures import LinkedList

def insertionSort(linklist):
    node = linklist.head
    # Linked list is length 0 or 1, no sort needed
    if node is None or node.pointer is None:
        return node

    print(linklist)
    swaps = 0
    while node:
        # if node.pointer is None:

        next_node = node.pointer
        
        # Swap is required
        if node.data > next_node.data:
            # Move to root
            # node.pointer = next_node.pointer
            # next_node.pointer = node.pointer
            # node.head = next_node
            swap(next_node)
            swaps += 1

        print(linklist)
        node = node.pointer

    return linklist, swaps

def swap(node):
    # traverse list to find the spot where the node belongs
    cur = 
    while search:




