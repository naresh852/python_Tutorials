digit=int(input())
if digit>=0 and digit<=1000000:
    d={0:9,
       1:8,
       2:7,
       3:6,
       4:5,
       5:4,
       6:3,
       7:2,
       8:1,
       9:0}
    l=[int(y) for y in str(digit)]
    result=[]
    for i in l:
       for k,v in d.items():
            if i==k:
                result.append(v)
    for i in result:
        print(i,end="")
else:
    print("Wrong Input")
