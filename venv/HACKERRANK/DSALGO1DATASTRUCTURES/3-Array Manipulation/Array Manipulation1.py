#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'arrayManipulation' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

# def arrayManipulation(n, queries):
# Write your code here
# rows=len(queries)
def arrayManipulation(n, queries):
    array = [0] * (n + 1)

    for query in queries:
        a = query[0] - 1
        b = query[1]
        k = query[2]
        array[a] += k
        array[b] -= k

    max_value = 0
    running_count = 0
    for i in array:
        running_count += i
        if running_count > max_value:
            max_value = running_count

    return max_value

    # sublist=[0]*(n+1)

    # for i in range(rows):
    #         start=queries[i][0]
    #         stop=queries[i][1]
    #         add=queries[i][2]
    #         for j in range(start,stop+1):
    #             sublist[j]=sublist[j]+add
    # return  max(sublist)
    # big=float("-inf")
    # for i in queries:
    #     for j in range(i[0],i[1]+1):
    #         sublist[j]=sublist[j]+i[2]
    #         if sublist[j]>big:
    #             big=sublist[j]
    # return big


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
