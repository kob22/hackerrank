#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):

    if len(note) > len(magazine):
        return False

    magazine_counter = Counter(magazine)

    for word in note:
        if magazine_counter[word] > 0:
            magazine_counter[word] -= 1
        else:
            return False
    return True

if __name__ == '__main__':

    magazine = 'give me one grand today night'.rstrip().split()

    note = 'give one grand today'.rstrip().split()

    print(checkMagazine(magazine, note))

    magazine = 'two times three is not four'.rstrip().split()

    note = 'two times two is four'.rstrip().split()

    print(checkMagazine(magazine, note))

