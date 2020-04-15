#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the howManyGames function below.
#price p
#difference d
#minimum m
#starting amount s 
def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    count=0
    temp=0
    if s+m==p:
    while p>m :
        count+=1
        temp+=p
        p=p-d
        print(temp)
    temp=temp+m
    while temp<=s:
        count+=1
        temp=temp+m
        print(temp)
    else:
        return count
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    pdms = input().split()

    p = int(pdms[0])

    d = int(pdms[1])

    m = int(pdms[2])

    s = int(pdms[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
