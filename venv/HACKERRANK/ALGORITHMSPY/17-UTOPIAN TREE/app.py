#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'utopianTree' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def utopianTree(n):
    # Write your code here
    x=0
    l=[1]
    value=1
    while  x!=n:
        x=x+1
        if x%2!=0:
            value=value*2
            l.append(value)
        else:
            value=value+1
            l.append(value)
    return l[-1]
            # return (pow(2,(n+2)//2)-1 if n%2==0 else pow(2,(n+3)//2)-2)
#    def utopianTree(n):
#     if n < 3:
#         return n + 1
#     if n % 2 == 0:
#         return (utopianTree(n - 2) * 2) + 1
#     else:
#         return (utopianTree(n - 2) + 1) * 2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = utopianTree(n)

        fptr.write(str(result) + '\n')

    fptr.close()
