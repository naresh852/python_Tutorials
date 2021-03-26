n = int(input())

for _ in range(n):
    # assert n <= 1000
    re = 0
    li = []
    ele = int(input())
    # assert ele <=200000
    arr = list(input().split())
    arr1 = sorted(set(arr))
    arr2 = list(arr1)

    for i in arr2:
        col = []
        for j in range(ele):
            if i == arr[j]:
                bm = j+1
                col.append(bm)

        li.append(col)
    for i in range(len(li)):
        if len(li[i]) != 1:
            v = abs(max(li[i])-min(li[i]))
            re = re+v
    print(re)
