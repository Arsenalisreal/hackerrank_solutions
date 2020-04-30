#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def getDigit(n):
    x=[int(i) for i in str(n)]
    print(sum(x))
    if len(x)==1:
        return sum(x)
    else:
        return getDigit(sum(x))

def superDigit(n, k):
    p=str(n)*k
    m=getDigit(p)
    return m

'''
x = n * k % 9
print(x if x else 9)
'''


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
