# m,n=input().split()
# l=int(n)
# fi=int(m)
# # stop=int((m-1)/2)
# sr=".|."
# for i in range(fi+1):
#     od=int(i%2)
#     if i == fi:
#         print("WELCOME".center(l, "-"))
#         od=0
#     if od !=0:
#         print((sr*i).center(l,"-"))
#
# las=int(fi-1)
# for i in range(las):
#     j=int(las-i)
#     od=int(j%2)
#     if od!=0:
#         print((sr*j).center(l,"-"))

N, M = map(int,input().split())
for i in range(1,N,2):
    print(i)
    print((i * ".|.").center(M, "-"))
print("WELCOME".center(M,"-"))
for i in range(N-2,-1,-2):
    print((i * ".|.").center(M, "-"))
for i in range(N-2,-1,-2):
    print(i)
print("\n")
for j in range(9,0,-1):
    print(j)