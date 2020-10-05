#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#


def countingValleys(steps, path):
    level = 0
    valleys = 0

    for step in path:
        if step == 'D':
            level -=1
        elif step == 'U':
            level +=1

        # A valley is a sequence of consecutive steps below sea level,
        # starting with a step down from sea level and ending with a step up to sea level.
        if level == 0 and step == 'U':
            valleys +=1

    return valleys


if __name__ == '__main__':

    steps = 8

    path = 'DDUUDDUDUUUD'

    result = countingValleys(steps, path)

    print(result)
