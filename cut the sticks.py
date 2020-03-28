# pikachu
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cutTheSticks function below.
def cutTheSticks(arr):
    x=[]
    x.append(len(arr))
    while(len(arr)!=1):
        arr=[abs(min(arr)-i) for i in arr]
        if arr.count(0)==len(arr):
            break
        while 0 in arr:
            arr.remove(0)
        else:
            x.append(len(arr))
    return x

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
