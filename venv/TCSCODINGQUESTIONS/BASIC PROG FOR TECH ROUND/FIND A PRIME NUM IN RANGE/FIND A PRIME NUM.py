#PRIME NUMBER IS A NATURAL NUMBER WHICH IS GREATER THAN 1 AND IS DIVISOR OF 1 AND ITSELF ONLY
mini=int(input())
maxi=int(input())
for num in range(mini,maxi+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)