class Solution:
    def partition(self, arr, low, high):
        i = (low - 1)  # index of smaller element
        pivot = arr[high]  # pivot

        for j in range(low, high):
            if arr[j] <= pivot:
                i = i + 1
                arr[i], arr[j] = arr[j], arr[i]

        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1


    def quickSort(self, arr, low, high):
        if len(arr) == 1:
            return arr
        if low < high:
            pi = Solution.partition(self, arr, low, high)
            Solution.quickSort(self, arr, low, pi - 1)
            Solution.quickSort(self, arr, pi + 1, high)
'''
class Solution:
    def quickSort(self,arr, low, high):
        def partition(arr, low, high):
            i = (low-1)		 # index of smaller element
            pivot = arr[high]	 # pivot
            for j in range(low, high):
                if arr[j] <= pivot:
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]

            arr[i+1], arr[high] = arr[high], arr[i+1]
            return i+1
        if len(arr) == 1:
            return arr
        if low < high:
            pi = partition(arr, low, high)
            Solution().quickSort( arr, low, pi - 1)
            Solution().quickSort( arr, pi + 1, high)
            # Solution.quickSort(self,arr, low, pi-1)
            # Solution.quickSort(self,arr, pi+1, high)'''


if __name__ == "__main__":
    n=int(input())
    arr=list(map(int,input().split()))
    Solution().quickSort(arr,0,n-1)
    print(arr)
