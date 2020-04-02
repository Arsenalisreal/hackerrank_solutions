#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the theLoveLetterMystery function below.
def pos(a):
    s='abcdefghijklmnopqrstuvwxyz'
    for i in range(0,len(s)-1):
        if s[i]==a:
            return i

def theLoveLetterMystery(s):
    count=0
    if s[::-1]==s:
        return 0
    for i in range(0,len(s)//2):
        count+= abs(ord(s[i]) - ord(s[len(s) - i - 1]))
    #for i in range(len(s) // 2):
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = theLoveLetterMystery(s)

        fptr.write(str(result) + '\n')

    fptr.close()
