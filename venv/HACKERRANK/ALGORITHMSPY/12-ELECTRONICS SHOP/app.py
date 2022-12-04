#!/bin/python3

import os
import sys
from itertools import combinations


# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    maxi = -1
    result = 0
    for i in keyboards:
        for j in drives:

            if i + j <= b and i + j > maxi:
                maxi = i + j
    result = maxi
    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()

# return max((s for s in (k+d for k in keyboards for d in drives) if s<=b), default=-1)