
# def add(x,n):
#     sum=0
#     for i in range(x,x+m):
#         sum=sum+s[i]
#     return sum
#
# n=int(input())
# s=list(map(int,input().split()))
# d,m=map(int,input().split())
# times=n-(m-1)
# # print(times)
# # sum=0
# ways=0
# for i in range(times):
#     summ=add(i,n)
#     if summ==d:
#         ways=ways+1
# print(ways)


#!/bin/python3

import math
import os
import random
import re
import sys
def add(x,n):
    sum=0
    for i in range(x,x+m):
        sum=sum+s[i]
    return sum
def birthday(s, d, m):
    times=n-(m-1)
    ways=0
    for i in range(times):
       summ=add(i,n)
       if summ==d:
          ways=ways+1
    return ways
if __name__ == '__main__':
    fptr = open("ways.txt", 'a')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    dm = input().rstrip().split()

    d = int(dm[0])

    m = int(dm[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
