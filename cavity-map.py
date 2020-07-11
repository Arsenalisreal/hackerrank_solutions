#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the cavityMap function below.
def cavityMap(m):
    n=len(m)
    for i in range(n):
        for j in range(n):
            if not(i in [0,n-1] or j in [0,n-1]):
                c=m[i][j]
                if m[i-1][j]<c and m[i+1][j]<c and m[i][j-1]<c and m[i][j+1]<c:
                    tmep=list(m[i])
                    tmep[j]='x'
                    temp=''
                    for j in tmep:
                        temp+=j
                    m[i]=temp
    return m



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
