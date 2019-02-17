#!/usr/bin/env python
# 2019-1-18

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

    sorted_items = InsertionSort(items)
    print(sorted_items)