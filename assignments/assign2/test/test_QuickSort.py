#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
sys.path.append('.')
from Sorts.Quick import QuickSort

class TestMergeSort:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')

    quick = QuickSort(items)
    sorted_items = quick.sort()
    print(sorted_items, quick.swaps)