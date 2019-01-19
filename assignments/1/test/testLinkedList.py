#!/usr/bin/env python
# 2019-1-18

import sys
import pytest
from src import LinkedList

class TestLinkedList:
    new_list = LinkedList()

    def testNewLinkedList(self):
        self.new_list = LinkedList()
        assert self.new_list.head == None

    def testAddNode(self):
        self.new_list.addNode('node_1')
        assert self.new_list.head.data == 'node_1'

    def testGetLength(self):
        size = self.new_list.length()
        assert size == 1
        self.new_list.addNode('node_2')
        size = self.new_list.length()
        assert size == 2

    def testDelNode(self):
        node = self.new_list.delNode
        assert self.new_list.length() == 1
        assert node.data == 'node_2'

