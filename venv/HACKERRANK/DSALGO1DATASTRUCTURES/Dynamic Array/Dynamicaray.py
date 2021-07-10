#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#

def dynamicArray(n, queries):
    # Write your code here
    temparr = []
    answerarray = []
    for j in range(n):
        l = []
        temparr.append(l)

    lastanswer = 0
    querylen = len(queries)
    for i in range(querylen):
        if queries[i][0] == 1:
            idx = (queries[i][1] ^ lastanswer) % n
            temparr[idx].append(queries[i][2])
        else:
            idx = (queries[i][1] ^ lastanswer) % n
            value = temparr[idx][queries[i][2] % len(temparr[idx])]
            lastanswer = value
            answerarray.append(lastanswer)
    return answerarray


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
