#!/usr/bin/env python
# 2019-2-17

import os
import sys
import pytest
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

    print(hashtable.get(4))
   