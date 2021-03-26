def merge(arr, l, m, h):
    n1 = m - l + 1
    n2 = h - m
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(n1):
        L[i] = arr[i + l]
    for j in range(n2):
        R[j] = arr[j + m + 1]
    i = j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def mergesort(arr, l, h):
    if l < h:
        m = (l + h) // 2
        mergesort(arr, l, m)
        mergesort(arr, m + 1, h)
        merge(arr, l, m, h)


# arr=list(map(int,input().split()))

arr = [12, 11, 13, 5, 6, 7]
n = len(arr)
mergesort(arr, 0, n - 1)
for i in range(n):
    print(arr[i], end=" ")
# def mergesort(arr,l,h):
#     if l<h:
#         m=(l+h)//2
#         mergesort(arr,l,m)
#         mergesort(arr,m+1,h)
#         merge(arr,l,m,h)
# def merge(arr,l,m,h):
#     n1=m-l+1
#     n2=h-m
#     L=[0]*(n1)
#     R=[0]*(n2)
#     for i in range(n1):
#         L[i]=arr[i+l]
#     for j in range(n2):
#         R[j]=arr[j+m+1]
#     i=j=0
#     k=l
#     while i<n1 and j<n2:
#         if L[i]<=R[j]:
#             arr[k]=L[i]
#             i+=1
#         else:
#             arr[k]=R[j]
#             j+=1
#         k+=1
#     while i<n1:
#         arr[k]=L[i]
#         i+=1
#         k+=1
#     while j<n2:
#         arr[k]=R[j]
#         j+=1
#         k+=1

# mergesort but simplier
# def mergesort(arr):
#     if len(arr) > 1:
#         m = len(arr) // 2
#         L = arr[:m]
#         R = arr[m:]
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
#             else:
#                 arr[k] = R[j]
#                 j += 1
#             k += 1
#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1
#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1
# arr = [12, 11, 13, 5, 6, 7]
# mergesort(arr)
# for i in arr:
#     print(i, end=" ")
