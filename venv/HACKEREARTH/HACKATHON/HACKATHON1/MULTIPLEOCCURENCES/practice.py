n=int(input())
for i in range(n):
    arr=list(input().split())
    arr1=sorted(set(arr))
    arr2=list(arr1)

print(arr2)
print(arr2[0])