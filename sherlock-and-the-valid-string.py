#!/bin/python3

import math
import os
import random
import re
from collections import Counter
import sys

# Complete the isValid function below.
def isValid(s):
    b=Counter(list(s))
    c=list(set(s))
    x=0
    for i in range(1,len(c)):
        print(b[c[i]])
        print(c[i])
        if b[c[i]]!=b[c[i-1]] and x<2:
            x=x+1
        else:
            return "NO"
    return "YES"
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = isValid(s)

    fptr.write(result + '\n')

    fptr.close()
