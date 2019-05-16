#!/usr/bin/env python3
# 2019-5-5

class GreedyAlgorithm:
    def __init__(self, spices, knapsack):
        self.__spices = spices
        self.__knapsack = knapsack
        self.fillKnapsack()

    @property
    def knapsack(self):
        return self.__knapsack

    @knapsack.setter
    def knapsack(self, knapsack):
        self.__knapsack = knapsack

    def fillKnapsack(self):
        spice = self.__spices.head
        while spice is not None:
            # try to add the spice in its entirety to the Knapsack,
            if (self.knapsack.cur_quantity + int(spice.data.quantity)) <= int(self.knapsack.capacity):
                self.knapsack.cur_quantity += int(spice.data.quantity)
                self.knapsack.value +=  int(spice.data.quantity) * float(spice.data.price)
                print(f'added {spice.data.name}; q={spice.data.quantity}; v={ int(spice.data.quantity) * float(spice.data.price)}')

            # if it will cause an overflow, add a fraction of it
            else:
                remaining_capacity = int(self.knapsack.capacity) - self.knapsack.cur_quantity 
                fraction_of_spice = remaining_capacity % int(spice.data.quantity)
                self.knapsack.cur_quantity += fraction_of_spice
                self.knapsack.value += fraction_of_spice * float(spice.data.price)
                print(f'added {spice.data.name}; q={fraction_of_spice}; v={fraction_of_spice * float(spice.data.price)}')
           
            spice = spice.pointer

            self.knapsack.value = round(self.knapsack.value, 2)
            