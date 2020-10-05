#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the twoStrings function below.
def twoStrings(s1, s2):
    set_s1 = set(s1)
    set_s2 = set(s2)

    strings_intersection = set_s1.intersection(set_s2)

    if strings_intersection:
        return True
    return False

if __name__ == '__main__':

    s1 = 'hi'
    s2 = 'world'

    print(twoStrings(s1, s2))

