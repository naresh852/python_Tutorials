
# Online Python - IDE, Editor, Compiler, Interpreter

a=list(map(int,input().split()))
limit=int(input())
s,e=0,len(a)-1
c=0
while(s<=e):
    if a[s]+a[e]<=limit:
        s+=1
    e=e-1
    c+=1
print(c)