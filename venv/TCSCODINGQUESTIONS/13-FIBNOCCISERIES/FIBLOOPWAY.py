#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'sumOfNFibonacciNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def sumOfNFibonacciNumbers(n):
    # Write your code here
    n1, n2 = 0, 1
    l = []
    if n == 1:
        l.append(0)
    elif n == 2:
        l.append(1)
    else:
        for i in range(n):
            l.append(n1)
            s = n1 + n2
            n1 = n2
            n2 = s

    return sum(l)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = sumOfNFibonacciNumbers(n)

    fptr.write(str(result) + '\n')

    fptr.close()
