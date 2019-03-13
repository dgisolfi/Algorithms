#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
import random
sys.path.append('.')
from DataStructures.HashTable import HashTable

class TestInsertionSort:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')

    # Create a instance of my hash 
    # table to the specified length
    hashtable = HashTable(255)
    for item in items:
        key = hashtable.put(item)


    randomly_selected_items = []
    # Choose 42 random Items of the file
    for i in range(0,42):
        randomly_selected_items.append(random.choice(items))

    comparison_results = []

    for desired_item in randomly_selected_items:
        hashtable.get(desired_item)
        gets_n_comparisons = 1 + hashtable.comparisons
        comparison_results.append(gets_n_comparisons)
        # reset comparison counter
        hashtable.setComparisons = 0
        
        print(f'Found "{desired_item}" in list after {gets_n_comparisons} lookups and comparisons')
    
    # compute the average comparisons needed to find the item
    average = sum(comparison_results)/len(comparison_results)
    print(f'The average case for all 42 searches was {average} comparisons')
   