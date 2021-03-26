from math import gcd
max=int(input())
child=int(input())
childnum=map(int,input().split())
count=0
for i in childnum:
    if gcd(max,i)!=1:
        count+=1
print(count)
# maxnum = int(input())
# childs = int(input())
# childnum = map(int, input().split())
# count = 0
#
# for i in childnum:
#     if gcd(maxnum, i) != 1:
#         count = count + 1
#
# print(count)