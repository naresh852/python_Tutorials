#armstrong number is a n digits number which is equal to the sum of the nth power of its digits
for i in range(1001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if result==num:
        print(str(result)+ 'is armstrong')