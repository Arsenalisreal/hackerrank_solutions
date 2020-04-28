#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    mem=[]
    n=abs(len(arr)-len(brr))
    for i in arr:
        if brr.count(i)!=arr.count(i) and i not in mem:
            mem.append(i)
    for j in brr:
        if brr.count(j)!=arr.count(j) and j not in mem and len(mem)<=n:
            mem.append(j)
    return sorted(mem)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
