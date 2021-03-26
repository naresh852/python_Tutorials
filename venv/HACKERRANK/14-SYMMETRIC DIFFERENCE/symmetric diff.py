n1=int(input())
a1=set(map(int,input().split()))
n2=int(input())
a2=set(map(int,input().split()))
r1=list(a1.difference(a2))
r2=list(a2.difference(a1))
for i in r2:
    r1.append(i)
lil=sorted(r1)
for j in lil:
    print(j)
print([j for j in lil])

print(a1^a2)

a,b = [set(input().split()) for _ in range(4)][1::2]
print('\n'.join(sorted(a^b, key=int)))

# L = ["cccc", "b", "dd", "aaa"]
#
# print("Normal sort :", sorted(L))
#
# print("Sort with len :", sorted(L, key=len))