#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

def viralAdvertising(n):
    x = 1
    receipents = 5
    liked = [receipents // 2]
    while x != n:
        x = x + 1
        receipents = (receipents // 2) * 3
        liked.append(receipents // 2)
    return sum(liked)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()
