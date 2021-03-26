req=int(input())
i=input()
names=[]
while(i!='q' and i!='Q'):
    names.append(i)
    i=input()
n=len(names)
numbers=[]
for i in range(n):
    numbers.append(float(input()))
for i in range(n-1):
    for j in range(n-i-1):
        if numbers[j]<numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            names[j],names[j+1]=names[j+1],names[j]
for i in range(req):
    print(names[i])