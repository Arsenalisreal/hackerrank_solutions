#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def countele(s):
    a=set(s)
    if len(a)!=2:
        return False
    for i in range(len(s)-2):
        if s[i]!=s[i+2]:
            return False
    return True

def alternate(s):
    if len(s)==2 and s[0]!=s[1]:
        return 2
    m=set(s)
    for i in m:
        if s.count(i)==1:
            s=s.replace(i,'')
    m=set(s)
    #print(m)
    maxi=0
    for i in m:
        for j in m:
            d=set(i+j)
            ans=''.join([c for c in s if c in d])
            print(ans)
            if countele(ans) and len(ans)>maxi:
                maxi=len(ans)
         
    return maxi



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
