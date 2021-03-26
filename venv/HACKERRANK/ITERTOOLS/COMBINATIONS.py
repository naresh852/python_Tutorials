from itertools import combinations
if __name__ == '__main__':
    s,n =input().split()
    k="".join(sorted(s))
    num=int(n)
    for i in range(1,num+1):
        for j in combinations(k,i):
            print("".join(j))


# from itertools import *
# if __name__ == '__main__':
#     s,n=input().split()
#     nu=int(n)
#     k="".join(sorted(s))
#     for i in range(1,nu+1):
#         data=["".join(j) for j in combinations(k,i)]
#         print("\n".join(data))