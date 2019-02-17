#!/usr/bin/env python3
# 2019-1-18

import os
import sys
import requests
# print(os.getcwd())
sys.path.append('..')
from assign_1.DataStructures import LinkedList
from Sorts.Insertion import insertionSort
from Sorts.Merge import Merge
from Sorts.Quick import Quick

class Sort:
    def __init__(self):
        self.magicitems = LinkedList()

    def getMagicItems(self):
        try:
            session = requests.Session()
            response = session.get('http://labouseur.com/courses/algorithms/magicitems.txt')
            if response.status_code != 200:
                raise ValueError(f'ERROR: issue retriving data, status code for request: {response.status_code}')

            for item in response.text.splitlines():
                self.magicitems.addNode(item)

        except:
            raise ValueError('Request to retrieve magic items failed!')

    # def InsertSort(self):






if __name__ == "__main__":
   sort = Sort()
   sort.getMagicItems()
   sort.InsertSort()