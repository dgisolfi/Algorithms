#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
sys.path.append('.')
from Sorts.Selection import SelectionSort

class TestSelectionSort:
    items = []
    try:
        items = open('./test/MagicItems.txt').read().splitlines() 
    except:
        raise ValueError('File not found')

    selection = SelectionSort(items)
    sorted_items = selection.sort()
    print(sorted_items, selection.swaps)