#!/usr/bin/env python
# 2019-1-18

import pytest
from DataStructures.Queue import Queue

class TestQueue:
    q = Queue()

    def testEnqueue(self):
        assert self.q.length() == 0
        self.q.enqueue('msg_1')
        assert self.q.length() == 1
        self.q.enqueue('msg_2')

    def testGetLength(self):
        assert self.q.length() == 2
      
    def testDequeue(self):
        message = self.q.dequeue()
        # Should be the first element added to queue
        assert message == 'msg_1'

    def testQueuePrint(self):
        print(self.q)
