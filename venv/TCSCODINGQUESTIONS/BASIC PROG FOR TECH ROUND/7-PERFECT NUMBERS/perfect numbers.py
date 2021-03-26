#A PERFECT NUM IS A POSITIVE NUMBER WHICH IS EQUAL TO SUM OF ITS POSITIVE DIVISORS EXCEPT THE NMBER ITSELF
n=int(input())
res=0
for i in range(1,n):
    if n%i==0:
        res=res+i
if res==n:
    print('perfect num')
else:
    print('not perfect')
