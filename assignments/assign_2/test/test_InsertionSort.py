#!/usr/bin/env python
# 2019-1-18

import os
import sys
import pytest
print(os.getcwd())
sys.path.append('.')
from Sorts.Insertion import Insertion

sys.path.append('..')
from assign_1.DataStructures import LinkedList

class TestInsertionSort:
    linked_list = LinkedList()
    try:
        file = open('./test/MagicItems.txt')
        lines = file.read().splitlines()
        for line in lines:
            linked_list.addNode(line)

    except:
        raise ValueError('File not found')

    sort = Insertion(linked_list)

    def runSort(self):
        print(self.linked_list.head())
        self.sort.traverseList(self.sort.linked_list.head())