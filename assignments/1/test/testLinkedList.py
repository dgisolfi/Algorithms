#!/usr/bin/env python
# 2019-1-18

import os
import sys
import pytest
sys.path.append('...')
print(os.getcwd())
from DataStructures.LinkedList import LinkedList

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
        self.new_list.addNode('node_3')
        self.new_list.addNode('node_4')

    def testStr(self):
        print(self.new_list)

    def testDelOldestNode(self):
        node = self.new_list.delOldestNode()
        assert self.new_list.length() == 3
        assert node.data == 'node_1'

    def testDelNewestNode(self):
        node = self.new_list.delNewestNode()
        assert self.new_list.length() == 2
        assert node.data == 'node_4'
    
   

