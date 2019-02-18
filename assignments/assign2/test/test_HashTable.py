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

    hashtable = HashTable(len(items))
    for item in items:
        key = hashtable.put(item)


    randomly_selected_items = []
    # Choose 42 random Items of the file
    for i in range(0,42):
        randomly_selected_items.append(random.choice(items))

    
    lookups = 0
    for desired_item in randomly_selected_items:
        # hashtable.get()
        lookups += 1
        
        print(f'Found "{desired_item}" at index: location'
        + f' in list after {lookups} comparisons')
    
    # compute the average comparisons needed to find the item
    # average = sum(comparisons)/len(comparisons)
    print(f'The average case for all 42 searches was {average} comparisons')
   