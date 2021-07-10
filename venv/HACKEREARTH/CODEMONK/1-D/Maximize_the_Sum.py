# https://github.com/jaggaroshu/i-practice_data-structure./blob/master/maximize_the_sum.py
n=int(input())
for i in range(n):
    N,k=map(int,input().split())
    Arr1=list(map(int, input().split()))
    Arr=[]
    for i in Arr1:
            if i>0:
                Arr.append(i)

    arr=sorted(Arr,key=int,reverse=True)
    nset=set(arr)
    nlist=list(nset)
    nlist=sorted(nlist,key=int,reverse=True)
    x=0
    for j in range(k):
        if nlist[j] > 0:
           cont=arr.count(nlist[j])
           x=x+(nlist[j]*cont)
        else:
           break
    print(x)
    arr.clear()
    nlist.clear()
#   WORKS FINE USES DIC
tests = int(input())
for _ in range(tests):
   [N, K] = [int(x) for x in input().split()]
   A = [int(x) for x in input().split()]
   Dict = {}
# Creating dict of only positive integers with value as sum
   for num in A:
      if num > 0:
        if num not in Dict:
          Dict[num] = num
        else:
         Dict[num] += num
# Extracting Sum from Dict
   values = []
   for x in Dict.values():
     values.append(x)
   values.sort()
   print(sum(values[-K:]))