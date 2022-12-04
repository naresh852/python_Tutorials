#!/bin/python3

import math
import os
import random
import re
import sys

# #
# # Complete the 'circularArrayRotation' function below.
# #
# # The function is expected to return an INTEGER_ARRAY.
# # The function accepts following parameters:
# #  1. INTEGER_ARRAY a
# #  2. INTEGER k
# #  3. INTEGER_ARRAY queries
# #

# def circularArrayRotation(a, k, queries):
#     # Write your code here

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     first_multiple_input = input().rstrip().split()

#     n = int(first_multiple_input[0])

#     k = int(first_multiple_input[1])

#     q = int(first_multiple_input[2])

#     a = list(map(int, input().rstrip().split()))

#     queries = []

#     for _ in range(q):
#         queries_item = int(input().strip())
#         queries.append(queries_item)

#     result = circularArrayRotation(a, k, queries)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
n, k, q = map(int, input().split())
arr = list(map(int, input().split()))
que = []
for i in range(q):
    print(arr[(int(input()) + n - k) % n])
    # rotation=(k-1)%n+1
# if rotation!=n:
#   for i in range(rotation):
#     temp=arr
#     last=temp[-1]
#     remaining=temp[0:len(arr)-1]
#     arr=[last]+remaining
# else:
#     arr=arr

# for i in que:
#     print(arr[i])
