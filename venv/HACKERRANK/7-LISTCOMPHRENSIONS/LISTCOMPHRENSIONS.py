x=int(input())
y=int(input())
z=int(input())
n=int(input())
friends=[]
for index in range(0,x+1):
    for inde in range(0,y+1):
        for ind in range(0,z+1):
            col=[]
            if index+inde+ind != n:
                 col.append(index)
                 col.append(inde)
                 col.append(ind)
                 friends.append(col)

print(friends)