#to print triangle right angle
n=int(input())
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(n,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()
#to print pyramid
for i in range(n):
    for j in range(n-i-1):
        print(end=" ")
    for j in range(i+1):
        print('*',end=" ")
    print()

for i in range(n,0,-1):
    for j in range(n-i):
        print(end=" ")
    for j in range(i):
        print('*',end=" ")
    print()
#to print diamond
rows=n
for i in range(rows):
    print(' '*(rows-i-1)+'* '*(i+1))
for i in range(rows-1,0,-1):
    print(' '*(rows-i)+'* '*(i))

