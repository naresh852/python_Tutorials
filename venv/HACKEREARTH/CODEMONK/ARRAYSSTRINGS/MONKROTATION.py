n=int(input())
for i in range(n):
    N,K=map(int,input().split())
    l=list(map(str,input().split()))
    # ll="".join(l)
    col=[]
    K=K%N
    for i in range(N):
        col.append(l[(i+(N-K))%N])
    print(" ".join(col))