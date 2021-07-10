def insertion_sort(A):
    for i in range(1,len(A)):
        cur=A[i]
        k=i
        while k>0 and A[k-1]>cur:
            A[k]=A[k-1]
            k=k-1
        A[k]=cur
# def insertion_sort(A):
#
#    for k in range(1, len(A)): # from 1 to n-1
#        cur = A[k] # current element to be inserted
#        j=k # find correct index j for current
#        while j > 0 and A[j-1] > cur: # element A[j-1] must be after current
#           A[j] = A[j-1]
#           j -= 1
#        A[j] = cur

A=[5,4,8,9,26,4,5,0,23]
insertion_sort(A)
print(A)