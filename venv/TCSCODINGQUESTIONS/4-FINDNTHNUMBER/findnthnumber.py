n=int(input())
li=[1]
c2=c3=c5=0
i=0
while i<n:
    ne=min(2*li[c2],3*li[c3],5*li[c5])
    li.append(ne)
    if ne==2*li[c2]:
        c2+=1
    if ne==3*li[c3]:
        c3+=1
    if ne==5*li[c5]:
        c5+=1
    i+=1
print(li)
print(li[n-1])
