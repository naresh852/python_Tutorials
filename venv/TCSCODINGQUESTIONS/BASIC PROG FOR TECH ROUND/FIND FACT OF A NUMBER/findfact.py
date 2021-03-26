n=int(input())
fact=1
if n<0:
    print('fact doesnt exist for negative number')
elif n==0:
    result=1
else:
    for i in range(1,n+1):
        fact=fact*i
    result=fact
print(result)