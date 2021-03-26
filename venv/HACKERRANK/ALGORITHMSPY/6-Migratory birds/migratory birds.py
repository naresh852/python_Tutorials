#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    s = set(arr)
    l = len(s)
    a = {}
    m = []
    mi = []
    for i in s:
        c = arr.count(i)
        a[i] = c
        m.append(c)
    ma = max(m)
    for i in s:
        if a[i] == ma:
            mi.append(i)
    return min(mi)

if __name__ == '__main__':
    fptr = open("record.txt", 'a')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
