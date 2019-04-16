#!/usr/bin/env python
# 2019-3-31

import os
import sys
import pytest
import random
sys.path.append('.')
from BinarySearchTree.BinarySearch import BinarySearchTree

class TestBinarySearchTree:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')
    
    bst = BinarySearchTree()
    
    for item in items:
        bst.insert(item)

    randomly_selected_items = []
    # Choose 42 random Items of the file
    for i in range(0,42):
        randomly_selected_items.append(random.choice(items))

    comparisons = []

    for desired_item in randomly_selected_items:
        found_item = bst.search(desired_item)
        comparisons.append(bst.comparisons)
        print(f'Found "{desired_item}" in list after {bst.comparisons} comparisons')
    
    # compute the average comparisons needed to find the item
    average = round(sum(comparisons)/len(comparisons), 2)
    print(f'The average case for all 42 searches was {average} comparisons')