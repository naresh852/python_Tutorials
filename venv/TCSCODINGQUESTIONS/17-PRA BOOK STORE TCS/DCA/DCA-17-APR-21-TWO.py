total_count=int(input())
digits=[]
for i in range(total_count):
    digits.append(input())
result=[]
for j in digits:
    if j=="1":
        result.append(1)
for j in digits:
    if j=="0":
        result.append(0)
for j in digits:
    if j=="2":
        result.append(2)
print(*result)

# n=int(input())
# list=[]
# for _ in range(n):
#     list.append(int(input()))
# zeros=[]
# ones=[]
# twos=[]
# for i in list:
#     if (i==0):
#         zeros.append(i)
#     elif(i==1):
#         ones.append(i)
#     else:
#         twos.append(i)
# result=ones+zeros+twos
# for i in result:
#     print(i,end=" ")