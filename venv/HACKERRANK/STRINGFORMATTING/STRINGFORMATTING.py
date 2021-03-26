def value(n):
     results=[]
     for i in range(1,n+1):
         deci=str(i)
         octa=str(oct(i)[2:])
         hexa=str(hex(i)[2:].upper())
         binary=str(bin(i)[2:])
         results.append([deci,octa,hexa,binary])
     width=len(results[n-1][3])
     for i in results:
         print(*(rep.rjust(width) for rep in i))
     print(results[16][3])
n=int(input())
value(n)

