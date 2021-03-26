#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the breakingRecords function below.
def breakingRecords(scores):
    hcount = 0
    lcount = 0
    lowscore = scores[0]
    highscore = scores[0]
    for i in scores:
        if i > highscore:
            highscore = i
            hcount += 1
    for i in scores:
        if i < lowscore:
            lowscore = i
            lcount += 1
    return [hcount, lcount]


if __name__ == '__main__':
    fptr = open("records.txt", 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')


    fptr.close()
