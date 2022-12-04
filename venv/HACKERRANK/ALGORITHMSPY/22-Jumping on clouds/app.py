#!/bin/python3

import math
import os
import random
import re
import sys

n,k = map(int,input().split())
n=int(n)
k=int(k)
arr=list(map(int,input().split()))
e=100
i=0
# for i in range(0:len(arr):k):
jump=(i+k)%n
if jump==0:
    if arr[jump]==1:
        e=e-1-2
    else:
        e=e-1
    ans=e
while jump!=0:
   jump=(i+k)%n
   if arr[jump]==1:
      e=e-1-2
   else:
      e=e-1
   i=i+k
   ans=e

print(ans)
# Complete the jumpingOnClouds function below.
# def jumpingOnClouds(c, k):

# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     nk = input().split()

#     n = int(nk[0])

#     k = int(nk[1])

#     c = list(map(int, input().rstrip().split()))

#     result = jumpingOnClouds(c, k)

#     fptr.write(str(result) + '\n')

#     fptr.close()

def jumpingOnClouds(c):
    current_position = 0
    number_of_jumps = 0
    last_cloud_postion = len(c) - 1
    last_second_postion = len(c) - 2

    while current_position < last_second_postion:
        # Checking if the cloud next to the next cloud is thunderstorm
        if c[current_position + 2] == 0:
            current_position += 2
        else:
            current_position += 1
        number_of_jumps += 1
    # Checking if we are in the last cloud or the last second cloud
    if current_position != last_cloud_postion:
        number_of_jumps += 1

    return number_of_jumps


input()
c = list(map(int, input().split()))
print(jumpingOnClouds(c))