from collections import Counter
if __name__=='__main__':
    n=int(input())
    sizez=Counter(list(map(int,input().split())))
    print(sizez)
    custnum=int(input())
    summ=0
    for _ in range(custnum):
        size,cost=map(int,input().split())
        if sizez[size] != 0:
            summ=summ+cost
            sizez[size]=sizez[size]-1
        # else:
        #     sum=sum+0
    print(summ)


