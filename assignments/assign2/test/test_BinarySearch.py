#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
import random
sys.path.append('.')
from Sorts.Merge import MergeSort
from Searches.Binary import BinarySearch

class TestBinarySearch:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')
    
    # Sort the Elements of the list
    merge = MergeSort(items)
    items = merge.sort()

    randomly_selected_items = []
    # Choose 42 random Items of the file
    for i in range(0,42):
        randomly_selected_items.append(random.choice(items))

    comparisons = []

    for desired_item in randomly_selected_items:
        binary = BinarySearch(items, desired_item)
        location = binary.search()
        comparisons.append(binary.comparisons)
        print(f'Found "{desired_item}" at index: {location}'
        + f' in list after {binary.comparisons} comparisons')
    
    # compute the average comparisons needed to find the item
    average = sum(comparisons)/len(comparisons)
    print(f'The average case for all 42 searches was {average} comparisons')