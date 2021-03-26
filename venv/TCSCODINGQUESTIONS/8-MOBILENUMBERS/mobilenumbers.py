# x<10 or x>10
# x==int(x)
# ARRAY LENGTH <5 OR >5INPUTLIMIT 5
# output count of invalid numbers only
A=[]
i=0
c=0
while i!='q' and i!='Q':
    x=input()
    if x!='q' and x!='Q':
        A.append(x)
    i=x
n=len(A)
if n!=5:
    print("INPUT LIMIT IS 5")
else:
    # x=sorted(A,key=int)
    c=0
    for i in A:
        if len(i)!=10 and i.isdigit()==False:
            c+=1
    print(c)