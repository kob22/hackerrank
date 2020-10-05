#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k):
    sorted_prices = sorted(prices, reverse=True)
    left_money = k
    how_many =0
    while left_money >0 and sorted_prices:
        left_money-=sorted_prices.pop()
        how_many+=1
    if left_money < 0:
        how_many-=1
    return how_many
if __name__ == '__main__':

    n = 7

    k = 50

    prices = list(map(int, '1 12 5 111 200 1000 10'.rstrip().split()))

    result = maximumToys(prices, k)
    print(result)