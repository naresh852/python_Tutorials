#greatest common divisor of two numbers
#we use euclids algorithm to find agcd
import math
def gcdoftwo(a,b):
    if b==0:
        return a
    else:
        return gcdoftwo(b,a%b)
num1=int(input())
num2=int(input())
# res=math.gcd(num1,num2)
res=gcdoftwo(num1,num2)
print(res)
'''ex:12,6
divisors of 12 and 6
12-1,2,3,4,6,12
6-1,2,3,6 
common divisors are 1,2
among them greatest is 2'''