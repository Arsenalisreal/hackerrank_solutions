#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pairs function below.
def pairs(k, arr):
 count=0
    arr=sorted(set(arr))
    for i in arr:
        for j in arr:
            if i-j==k:
                count+=1
    return count
    #return len(set(arr) & set(x + k for x in arr))#Found this oneliner


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    arr = list(map(int, input().rstrip().split()))

    result = pairs(k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
