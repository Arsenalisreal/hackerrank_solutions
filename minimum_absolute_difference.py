#!/bin/python3

import math
import os
import random
import re
import sys
import itertools

# Complete the minimumAbsoluteDifference function below.
def minimumAbsoluteDifference(arr):
    arr.sort()
    mi=10**10
    for i in range(len(arr)-1):
        if abs(arr[i]-arr[i+1])<mi:
            mi=abs(arr[i]-arr[i+1])
    return mi
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = minimumAbsoluteDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
