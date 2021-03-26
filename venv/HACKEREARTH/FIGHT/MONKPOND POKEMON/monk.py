n=int(input())
for i in range(n):
    N=int(input())
    count=0
    l = []
    poi=[]
    for j in range(N):

        f,p=input().split()
        l.append(f)
        poi.append(p)
    sorted(l)
    sorted(poi)
    for o in range(N):
        if l.__contains__(poi[o]):
            l.remove(poi[o])
    print(len(l))

n=[1,2,2,3,3]
print(n)