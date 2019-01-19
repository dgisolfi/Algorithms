#!/usr/bin/env python
# 2019-1-18

import pytest
from DataStructures.Stack import Stack

class TestStack:
    s = Stack()

    def testPush(self):
        self.s.push('page_1')
        assert self.s.length() == 1

    def testPeek(self):
        page = self.s.peek()
        # should look at top of the stack without removing element
        assert page == 'page_1'
        assert self.s.length() == 1

    def testPop(self):
        self.s.push('page_2')
        page = self.s.pop()
        # Removes and returns the object at the top of the Stack.
        assert page == 'page_2'
        assert self.s.length() == 1

    def testClear(self):
        self.s.clear()
        assert self.s.length() == 0
