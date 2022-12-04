#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'saveThePrisoner' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. INTEGER s
#

# def saveThePrisoner(n, m, s):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     t = int(input().strip())

#     for t_itr in range(t):
#         first_multiple_input = input().rstrip().split()

#         n = int(first_multiple_input[0])

#         m = int(first_multiple_input[1])

#         s = int(first_multiple_input[2])

#         result = saveThePrisoner(n, m, s)

#         fptr.write(str(result) + '\n')

#     fptr.close()
def savetheprisoner(n, c, s):
    # if n>c:
    #     x=n%c
    #     s=s+x
    # # return s
    # elif n==c:
    #     s=s-1
    # # return s
    # else:
    #     x=c%n
    #     s=s+x-1
    # return s
    return ((c + s - 2) % n) + 1

    # return ans[-1]


t = int(input())
# x=[]
for i in range(t):
    n, c, s = map(int, input().split())
    y = savetheprisoner(n, c, s)
    print(y)



#!/usr/bin/env python3
#
# T = int(input().strip())
# for _ in range(T):
#     N,M,S = list(map(int, input().strip().split()))
#     print(((S - 1 + M - 1) % N) + 1)
# The S-1 translates the prisoner id to an equivalent index (since % effectively deals with indexes like 0..N-1). The M-1 handles the fact that the first prisoner to get a sweet is not counted when giving away sweets. Example, if you are giving away 1 sweet and you start at prisoner 37, it is 37 = (37 + 1 - 1) that should be warned. If you are giving away 2 sweets it is 38 = (37 + 2 - 1) that should be warned. And so on. The % N handles the wrapping around based on the index of the prisoners. And the + 1 brings us back to dealing with prisoner ID's instead of indicies.