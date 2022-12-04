
#take input
#constrains
#no - neagtive values
# if no one item then print 1


n=int(input())
dic={}
for i in range(n):
    j=int(input())
    assert j>=0
    dic[j]=dic.get(j,0)+1
print(dic)
lis=[]
for v in dic.values():
    lis.append(v)

if 1 not in lis:
    print(1)
else:
    for k,v in dic.items():
     if dic[k]==1:
        print(k)
        break

# num=int(input())
# arr = []
# for i in range(num):
#     arr.append(int(input()))
# length = len(arr)
# for i in range(length):
# 	j = 0
# 	while(j < length):
# 		if (i != j and arr[i] == arr[j]):
# 			break
# 		j += 1
# 	if (j == length):
# 	    print(arr[i])
# 	    break