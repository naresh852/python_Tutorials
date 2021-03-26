try:
    A=[]
    while True:
       i=input()
       assert int(i) >0 and int(i)<=120
       if i=="":
         break
       else:
         A.append(int(i))
    cost=0
    for i in A:
        if i<17:
           cost+=200
        elif 17<=i<=40:
           cost+=400
        else:
           cost+=300
    print(f"Total Income {cost} INR")
except:
    print("INVALID INPUT")

