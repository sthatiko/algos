

import math
import os
import random
import re
import sys

# https://www.hackerrank.com/challenges/encryption/problem


# Complete the encryption function below.
def encryption(s):
    my_s = s.replace(' ', '').strip('\n')
    s_length = len(my_s)
    _sroot = math.sqrt(s_length)
    rows = int(_sroot)
    cols = int(math.ceil(_sroot))
    while rows*cols < s_length:
        rows += 1
    itr = iter(my_s)
    op = [[0]*cols for i in range(rows)]
    count = 0
    for r in range(rows):
        for c in range(cols):
            if count == s_length:
                break
            op[r][c] = next(itr)
            count +=1
    my_s=''
    for c in range(cols):
        for r in range(rows):
            if op[r][c] != 0:
                my_s += op[r][c]
        my_s += ' '
    return my_s


if __name__ == '__main__':
    fptr = open(os.path.abspath(__file__)[:-2] + 'in', 'r')  # TODO: for local testing only
    sys.stdin = fptr
    s = sys.stdin.readline()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
