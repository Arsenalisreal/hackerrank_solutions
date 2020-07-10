#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the closestNumbers function below.
def closestNumbers(arr):
    arr=sorted(arr)
    l=[]
    f=100**100
    for i in range(len(arr)-1):
        u=abs(arr[i]-arr[i+1])
        if u<f:
            l=[]
            f=u
        if u==f:
            l.append(arr[i])
            l.append(arr[i+1])
    return l


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = closestNumbers(arr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
