#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):

    pos = 0
    jumps = 0
    while pos < len(c)-1:
        if pos+2 < len(c) and c[pos+2] == 0:
            pos +=2
        else:
            pos +=1
        jumps+=1

    return jumps


if __name__ == '__main__':

    n = 6

    c = list(map(int, '0 0 0 1 0 0'.rstrip().split()))

    result = jumpingOnClouds(c)

    print(result)