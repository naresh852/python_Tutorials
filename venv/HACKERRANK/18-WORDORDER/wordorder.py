# from collections import OrderedDict as o
# od=o()
# for _ in range(int(input())):
#     item=input()
#     od[item]=od.get(item,0)+1
# print(len(od))
# print(*od.values())

from collections import Counter
L=[]
for _ in range(int(input())):
    L.append(input())
x=Counter(L)
print(len(x))
print(*x.values())