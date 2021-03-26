
l=int(input())
u=int(input())
def armstrong(n):
    temp=n
    s=0
    l=len(str(temp))
    while(temp):
        digit=temp%10
        s=s+digit**l
        temp=temp//10
    if s==n:
        return True
    else:
        return False

if l<=0 or u<=0:
    print("wrong input")
else:
    for i in range(l,u+1):
        if (armstrong(i)):
            print(i)