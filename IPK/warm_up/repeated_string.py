#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):

    length_string = len(s)
    num_occur_a = s.count('a')

    # count full given string in infinite substring
    full_occur = n//length_string

    # rest of string
    rest = n%length_string

    total_occur = full_occur * num_occur_a + s[:rest].count('a')

    return total_occur


if __name__ == '__main__':
    s = 'aba'

    n = 10

    result = repeatedString(s, n)

    print(result)
