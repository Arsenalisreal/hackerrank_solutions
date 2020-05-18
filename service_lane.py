#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the serviceLane function below.
def serviceLane(n, cases):
    '''l=[]
    print(n)
    for i in cases:
        print(n[i[0]:i[1]+1])
        l.append(min(n[i[0]:i[1]]))
    return [min(n[i[0]:i[1]]) for i in cases]'''
    return [min(n[i[0]:i[1]+1]) for i in cases]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nt = input().split()

    n = int(nt[0])

    t = int(nt[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(width, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
