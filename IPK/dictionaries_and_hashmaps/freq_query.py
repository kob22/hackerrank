#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict, Counter
# Complete the freqQuery function below.

def freqQuery(queries):
    data = Counter()
    returned_array = []
    for query in queries:
        if query[0] == 1:
            data[query[1]]+=1
        elif query[0] == 2:
            if data[query[1]] >0:
                data[query[1]] -= 1
                if data[query[1]] == 0:
                    del data[query[1]]
        elif query[0] == 3:
            if query[1] in set(data.values()):
                returned_array.append(1)
            else:
                returned_array.append(0)

    return returned_array

if __name__ == '__main__':

    q = 10
    raw_input = "1 3 2 3 3 2 1 4 1 5 1 5 1 4 3 2 2 4 3 2"
    queries = []
    pair = []
    for i in raw_input.rstrip().split():
        pair.append(int(i))
        if len(pair) >1:
            queries.append(pair)
            pair = []

    ans = freqQuery(queries)
    print(ans)

