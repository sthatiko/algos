#!/bin/python3
import math
import os
import random
import re
import sys


# https://www.hackerrank.com/challenges/kaprekar-numbers/problem


# Complete the kaprekarNumbers function below.
def isKap(n):
    s = n*n
    _w = str(s)
    w = len(_w)
    _a = int(-w/2)
    a = _w[:_a]
    b = _w[_a:]
    if (int(a.strip() or 0)+int(b)) == n:
        return True
    return False

def kaprekarNumbers(p, q):
    valid = False
    result = ''
    for k in range(p,q+1):
        if isKap(k):
            result += str(k) + ' '
            valid = True
    if valid:
        print(result.rstrip(' '))
    else:
        print('INVALID RANGE')

if __name__ == '__main__':
    p = int(input())

    q = int(input())

    kaprekarNumbers(p, q)
