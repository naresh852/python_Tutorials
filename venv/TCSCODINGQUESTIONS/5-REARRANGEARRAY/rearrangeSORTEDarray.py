# t=int(input())
# while t:
#     n=int(input())
#     a=list(map(int,input().split()))
#     a.sort()
#     large=n-1
#     small=0
#     i=0
#     for i in range(n):
#         if i%2== 0:
#             print(a[large],end=" ")
#             large-=1
#         else:
#             print(a[small],end=" ")
#             small+=1
#     t=t-1

# Online Python - IDE, Editor, Compiler, Interpreter
n=int(input())
l=[]
for i in range(n):
    no=int(input())
    a=list(map(int,input().split()))
    if len(a)%2==0:
        x=0
    else:
        x=1
    while(len(a)>x):
        a.sort()
        l.append(a[-1])
        l.append(a[0])
        a.remove(a[-1])
        a.remove(a[0])
    if x==1:
        l.append(a[0])
    print(*l)
    l.clear()
