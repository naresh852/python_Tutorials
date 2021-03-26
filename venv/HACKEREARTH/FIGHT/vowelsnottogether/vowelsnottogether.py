# def solve(s):
#     leng=len(s)
#     total=combi(leng)
#     # print(total)
#     vowel="aeiou"
#     vcount=0
#     for i in vowel:
#         for j in range(leng):
#             if s[j]==i:
#                 vcount+=1
#     ccount=leng-vcount
# def repeat():
#
#
#
# def combi(num):
#     re=1
#     for i in range(1,num+1):
#         re=re*i
#
#     return re
#
# t=int(input())
# for _ in range(t):
#     s=input()
#     solve(s)

import math
import array
# total = array.array('i',[])
total=[]
i = 0
t = int(input())
vowel="aeiou"
while i<t :
    count = 0;
    s = input()
    for j in s :
        if j in vowel :
           count+=1
    cons = len(s) - count
    if cons==0:
        total.append(-1)
    else:
        factcons = math.factorial(cons)
        factvowl = math.factorial(count)
        factdiff = math.factorial(abs(cons-count))
        total.append(int(factcons*factvowl*(cons+1)*factcons/(factvowl*factdiff)))
    i+=1
for ele in total :
   print(ele)