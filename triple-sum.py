#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the triplets function below.

def triplets(a, b, c):
    a=list(sorted(set(a)))
    b=list(sorted(set(b)))
    c=list(sorted(set(c)))
    i=j=k=ans=0
    while j<len(b):
        while i<len(a) and a[i]<=b[j]:
            i+=1
        while k<len(c) and c[k]<=b[j]:
            k+=1
        ans+=i*k
        j+= 1
    return ans
    
        
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    lenaLenbLenc = input().split()

    lena = int(lenaLenbLenc[0])

    lenb = int(lenaLenbLenc[1])

    lenc = int(lenaLenbLenc[2])

    arra = list(map(int, input().rstrip().split()))

    arrb = list(map(int, input().rstrip().split()))

    arrc = list(map(int, input().rstrip().split()))

    ans = triplets(arra, arrb, arrc)

    fptr.write(str(ans) + '\n')

    fptr.close()
