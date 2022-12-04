#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#
n=int(input())
arr=list(map(int,input().split()))
arr2=arr
arr3=sorted(arr)
yvalues=[]
for i in range(len(arr)):
  for j in range(len(arr)):
    x=arr2[j]-1
    if arr[x] == arr3[i]:
        print(j+1)
# def permutationEquation(p):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     n = int(input().strip())

#     p = list(map(int, input().rstrip().split()))

#     result = permutationEquation(p)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
n=int(input())
fDict=dict()
fInvDict=dict()

L=input().split()
for i in range(n):
    fDict[i+1] = int(L[i])
    fInvDict[int(L[i])] = i+1
for x in range(1,n+1):
    print(fInvDict[fInvDict[x]])