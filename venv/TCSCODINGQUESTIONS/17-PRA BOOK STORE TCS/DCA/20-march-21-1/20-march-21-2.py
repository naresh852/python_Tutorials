from functools import reduce
n=input()

# lis=n.split()
nums=[]
for i in n:
    j=ord(i)
    nums.append(j)
print(reduce(lambda x,y:x^y,nums))



# str = input()
# len = len(str)
# result = ord(str[0])
# for i in range(1,len):
#     result = (result ^ (ord(str[i])))
# print(result)


#1+1=0
#0+0=0
#1+0=1
#0+1=1
