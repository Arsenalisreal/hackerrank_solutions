#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumDistances function below.
def find(a,x):
    l=[]
    for i in range(len(a)):
        if a[i]==x:
            l.append(i)
    return abs(l[0]-l[1])


def minimumDistances(a):
    x=9999
    g={}
    for i in range(len(a)):
        if a[i] not in g:
            g[a[i]]=i
        if a[i] in g:
            y=abs(i-g[a[i]])
            print(y)
            if y==0:
                continue
            else:
                x=min(x,y)
    print(g)
    if x==9999:
        return -1
    return x
    


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()
