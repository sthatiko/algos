import math
import os
import random
import re
import sys


# https://www.nayuki.io/page/next-lexicographical-permutation-algorithm
# https://www.hackerrank.com/challenges/bigger-is-greater/problem

# replace the rightmost occurrence
def rreplace(s, old, new):
    s = str(s)
    i = s.rfind(old)
    ret = s[:i] + new
    if i < len(s)-1:
        ret += s[i+1:]
    return ret


# Complete the biggerIsGreater function below.
def biggerIsGreater(w):
    if len(w) == 1:
        return 'no answer'
    sorted_w = sorted(set(w))
    prev = w[-1]  # last char
    pivot = -2  # last but one char
    for c in w[-2::-1]:  # start from last but one to beginning
        if sorted_w.index(c) >= sorted_w.index(prev):
            prev = c
            pivot -= 1
        else:
            break
    if -pivot > len(w):
        return 'no answer'  # given word is already the greatest string that can be formed with the letters.
    non_increasing_part = w[pivot+1:]
    for c in non_increasing_part[::-1]:  # find the least greatest char than pivot char
        if c > w[pivot]:
            gt_than_pivot = c
            break
    ret = w[:pivot] + gt_than_pivot + rreplace(non_increasing_part, gt_than_pivot, w[pivot])[::-1]
    return ret


if __name__ == '__main__':
    fptr = open(os.path.abspath(__file__)[:-2] + 'in', 'r')  # TODO: for local testing only
    sys.stdin = fptr

    T = int(sys.stdin.readline())
    results = ''

    for T_itr in range(T):
        w = sys.stdin.readline()
        w = w.rstrip('\n')
        result = biggerIsGreater(w)
        results += result + '\n'
    fptr.close()
    fptr = open(os.path.abspath(__file__)[:-2] + 'in', 'w')
    fptr.write(results.rstrip('\n'))
    fptr.close()
