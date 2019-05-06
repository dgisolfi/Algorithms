#!/usr/bin/env python3
# 2019-5-5

import sys
sys.path.append('..')
from assign4.FractionalKnapsack.parser import Parser
from assign4.FractionalKnapsack.GreedyAlgorithm import GreedyAlgorithm

parser = Parser('./test/spice.txt')

print(parser.spices)

parser.spices.deleteTail()

print(parser.spices)


for knapsack in parser.knapsacks:
    # alert of new knapsack
    # print(f'Preforming greedy solution on Fractional Knapsack with {knapsack}')
    pass