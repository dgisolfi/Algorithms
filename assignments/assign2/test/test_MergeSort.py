#!/usr/bin/env python
# 2019-1-18

import os
import sys
import pytest
sys.path.append('.')
from Sorts.Merge import MergeSort

class TestMergeSort:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')

    merge = MergeSort(items)
    sorted_items = merge.sort()
    print(sorted_items, merge.swaps)