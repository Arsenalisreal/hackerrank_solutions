#!/bin/python3

import math
import os
from collections import Counter
import sys

# Complete the gameOfThrones function below.
def gameOfThrones(s):
    c=Counter(list(s))
    s1=list(set(s))
    count=0
    for i in s1:
        if c[i]%2!=0:
            count+=1
            if count>2:
                return "NO"
                break
    return 'YES'
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
