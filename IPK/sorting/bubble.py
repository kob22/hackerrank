#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    swaps = 0
    for i in range(len(a)-1,0,-1):
        for j in range(i):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swaps+=1
    return(swaps,a[0],a[-1])

if __name__ == '__main__':
    n = 3

    a = [3,2,1]

    print(countSwaps(a))
