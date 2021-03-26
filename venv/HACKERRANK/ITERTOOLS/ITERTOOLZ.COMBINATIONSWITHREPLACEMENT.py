from itertools import *
if __name__ == '__main__':
    s,n=input().split()
    nu=int(n)
    k="".join(sorted(s))
    for j in combinations_with_replacement(k,nu):
        print("".join(j),sep="\n")
