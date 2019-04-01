#!/usr/bin/env python
# 2019-3-31

from .node import Node

class BinarySearchTree:
    def __init__(self):
        self.__root = None
        self.__comparisons = 0

    @property
    def comparisons(self):
        return self.__comparisons

    def __str__(self):
        if self.__root is not None:
            self.__printTree(self.__root)
        return ''

    def __printTree(self, cur_node):
        if cur_node is not None:
            self.__printTree(cur_node.left_child)
            print(cur_node.value)
            self.__printTree(cur_node.right_child)

    def insert(self, value):
        # check if the root can be used
        if self.__root is None:
            self.__root = Node(value)
        else:
            self.__insert(value, self.__root) 

    def __insert(self, value, cur_node):
        if value < cur_node.value:
            if cur_node.left_child is None:
                cur_node.setLeftChild(Node(value))
            else:
                self.__insert(value, cur_node.left_child)
        elif value > cur_node.value:
            if cur_node.right_child is None:
                cur_node.setRightChild(Node(value))
            else:
                self.__insert(value, cur_node.right_child)
        else:
            print('value in tree')

    def search(self,value):
        # reset the comparison value for new search
        self.__comparisons = 0
        if self.__root is not None:
            return self.__search(value, self.__root)
        else:
            return None
            
    def __search(self, value, cur_node):
        if value == cur_node.value:
            self.__comparisons += 1
            return cur_node
        elif value < cur_node.value and cur_node.left_child is not None:
            self.__comparisons += 2
            return self.__search(value,cur_node.left_child)
        elif value > cur_node.value and cur_node.right_child is not None:
            self.__comparisons += 3
            return self.__search(value,cur_node.right_child)