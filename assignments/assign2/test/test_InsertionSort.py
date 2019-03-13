#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
sys.path.append('.')
from Sorts.Insertion import InsertionSort

class TestInsertionSort:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')

    insertion = InsertionSort(items)
    sorted_items = insertion.sort()
    print(insertion.comparisons)