n = int(input())

for index in range(1,n+1):
    print(index,end="")##removes space
print()
print(*range(1,n+1))
print()
print(*range(1,n+1),sep="")##removes space
