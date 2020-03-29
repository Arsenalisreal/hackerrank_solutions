#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    s=list(s)
    t=list(t)
    arc=abs(len(s)-len(t))
    if arc>k:
        return 'No'
    count=0
    if len(s)>len(t):
        for i in range(len(t)-1):
            if s[i]!=t[i]:
                count+=1
    if len(s)<len(t):
        for i in range(len(s)-1):
            if s[i]!=t[i]:
                count+=1
    if len(s)==len(t):
        for i in range(len(s)-1):
            if s[i]!=t[i]:
                count+=1
    if count==1:
        return 'No'
    elif count+arc<=k:
        return 'Yes'
    else:
        return 'No'

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
