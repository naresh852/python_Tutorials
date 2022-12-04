#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    l = len(a)
    a.sort()
    # print(a)
    p = set(a)
    arr = []
    for pp in p:
        n = []
        for i in range(l):
            if abs(pp - a[i]) <= 1:
                n.append(a[i])
        arr.append(n)
    newlist = []
    for n in arr:
        l = len(n)
        if l > 1:
            pp = n[0]
            c = 1
            nn = []
            for j in range(1, l):
                if abs(pp - n[j]) >= 2:
                    break
                else:
                    c += 1
            newlist.append(c)

    # print(arr)
    # print(max(newlist))
    return max(newlist)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()


# from collections import Counter
# def pickingNumbers(a):
#     a = Counter(a)
#     maxi = 0
#     for k in sorted(a):
#         m = a[k]+a.get(k+1,0)
#         if maxi<m:
#             maxi=m
#     return maxi
# input()
# a = map(int,input().split())
# print(pickingNumbers(a))