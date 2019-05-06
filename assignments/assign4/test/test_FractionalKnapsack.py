#!/usr/bin/env python3
# 2019-5-5

import sys
sys.path.append('..')
from assign4.FractionalKnapsack.parser import Parser
from assign4.FractionalKnapsack.GreedyAlgorithm import GreedyAlgorithm
from assign4.FractionalKnapsack.SelectionSort import SelectionSort

parser = Parser('./test/spice.txt')

spices = parser.spices
# Sort the spices
sort = SelectionSort(spices)
spices = sort.elements

for knapsack in parser.knapsacks:
    # alert of new knapsack
    print(f'Preforming greedy solution on Fractional Knapsack with {knapsack}')
    greedy = GreedyAlgorithm(parser.spices, knapsack)
    print(f'Knapsack filled to {greedy.knapsack.cur_quantity}/{greedy.knapsack.capacity} with value={greedy.knapsack.value};\n')