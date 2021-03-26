#!/bin/python3

import os
import sys
from heapq import heapify, heappop, heappush


#
# Complete the cookies function below.
#

def cookies(k, A):
    heapify(A)
    c = 0
    try:
        while A[0] < k:
            c1 = heappop(A)
            c2 = heappop(A)
            f = int(c1 + 2 * c2)
            heappush(A, f)
            c += 1
        return c
    except:
        return "-1"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    A = list(map(int, input().rstrip().split()))

    result = cookies(k, A)

    fptr.write(str(result) + '\n')

    fptr.close()
