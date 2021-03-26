
# Online Python - IDE, Editor, Compiler, Interpreter
# a<b>c<d>e<f>g
n=int(input())
arr=list(map(int,input().split()))
flag=True
for i in range(n-2):
    if i%2==0:
        if arr[i]>arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    else:
        if arr[i]<arr[i+1]:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    
print(arr)