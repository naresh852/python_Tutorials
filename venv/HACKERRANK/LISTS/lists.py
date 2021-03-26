# N=int(input())
# lopi=[]
# i = "insert"
# r="remove"
# a="append"
# p="print"
# po="pop"
# re="reverse"
# so ="sort"
# count=0
# col=[]
# for _ in range(N):
#     stri,*num=input().split()
#     nums=list(map(int,num))
#     if stri==i:
#         lopi.insert(nums[0],nums[1])
#     elif stri==a:
#         lopi.append(nums[0])
#     elif stri==r:
#         lopi.remove(nums[0])
#     elif stri==po:
#         lopi.pop()
#     elif stri==re:
#         lopi.reverse()
#     elif stri==p:
#         x=lopi.copy()
#         col.append(x)
#         count+=1
#     else:
#         lopi.sort()
# # print(count)
# for index in range(count):
#     if count>=1:
#       print(col[index])
# i=int(input())
# lil=[]
# for _ in range(i):
#     name,*num=input().split()
#     nums=map(int,num)
#     if name=="print":
#         print(lil)
#     else:
#         getattr(lil,name)(*(nums))
l=['A','D','A']
l.pop(2)
print(l)
lk=['A','D','A']
lk.remove(lk[2])
print(lk)




# print(lopi)