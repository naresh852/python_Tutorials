
size=input()
lis=[]
for i in range(int(size)):
    j=int(input())
    lis.append(j)
    if lis.count(j) >1:
        print("INVALID INPUT")
        break
lis.sort(reverse=True)
N=int(input())
print(lis[N-1])

# array_size = int(input())
# A = []
#
# for i in range(array_size):
#     A.append(int(input()))
#
# nth = int(input())
#
# A.sort()
#
# temp = True
#
# for i in range(array_size - 1):
#     if A[i] == [i + 1]:
#         temp = False
#         break
#
# if temp:
#     print
#     A[len(A) - nth]
# else:
#
#     print('INVALID INPUT')