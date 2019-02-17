#!/usr/bin/env python3
# 2019-1-18
import time
import requests
from DataStructures.Queue import Queue
from DataStructures.Stack import Stack

class Palindrome:
    def __init__(self):
        self.magicitems = []
        self.palindrones = []

    def getMagicItems(self):
        # try:
        #     session = requests.Session()
        #     response = session.get('http://labouseur.com/courses/algorithms/magicitems.txt')
        #     if response.status_code != 200:
        #         raise ValueError(f'ERROR: issue retriving data, status code for request: {response.status_code}')

        #     for item in response.text.splitlines():
        #         self.magicitems.append(item)

        # except:
        #     raise ValueError('Request to retrieve magic items failed!')

        try:
            file = open('./big.txt')
            items = file.read().splitlines()
            for item in items:
                self.magicitems.append(item)

        except:
            raise ValueError('File not found')

    
    def stackChars(self, item):
        s = Stack()
        for char in list(item):
            s.push(char)
        return s
        
    def queueChars(self, item):
        q = Queue()
        for char in list(item):
            q.enqueue(char)
        return q

    def checkForPalindrone(self):
        for item in self.magicitems:
            magic_item = item.lower()
            magic_item = ''.join(magic_item.split())
            stacked_item = self.stackChars(magic_item)
            queued_item = self.queueChars(magic_item)

            s_word = ''
            q_word = ''
            for i in range(len(magic_item)):
                s_word += stacked_item.pop()
                q_word += queued_item.dequeue()

            if s_word == q_word:
                self.palindrones.append(item)

if __name__ == "__main__":
   palindrome = Palindrome()
   palindrome.getMagicItems()
   palindrome.checkForPalindrone()
   print(palindrome.palindrones)