#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
import random
sys.path.append('.')
from Searches.Linear import LinearSearch

class TestLinearSearch:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')

    randomly_selected_items = []
    # Choose 42 random Items of the file
    for i in range(0,42):
        randomly_selected_items.append(random.choice(items))

    comparisons = []

    for desired_item in randomly_selected_items:
        linear = LinearSearch(items, desired_item)
        location = linear.search()
        comparisons.append(linear.comparisons)
        print(f'Found "{desired_item}" at index: {location}'
        + f'in list after {linear.comparisons} comparisons')
    
    # compute the average comparisons needed to find the item
    average = sum(comparisons)/len(comparisons)
    print(f'The average case for all 42 searches was {average} comparisons')