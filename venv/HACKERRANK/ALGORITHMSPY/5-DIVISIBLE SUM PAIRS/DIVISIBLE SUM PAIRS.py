# n,k=map(int,input().split())
# a=list(map(int,input().split()))
# l=int(n-1)
# count=0
# for i in range(l):
#     first=a[i]
#     for j in range(i+1,n):
#         next=a[j]
#         if (first+next)%k == 0:
#             count=count+1
#
# print(count)

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the divisibleSumPairs function below.
def divisibleSumPairs(n, k, ar):
    l=int(n-1)
    count=0
    for i in range(l):
        first=ar[i]
        for j in range(i+1,n):
            next=ar[j]
            if (first+next)%k == 0:
                count=count+1
    return count

if __name__ == '__main__':
    fptr = open("demo.txt", 'a')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    ar = list(map(int, input().rstrip().split()))

    result = divisibleSumPairs(n, k, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
