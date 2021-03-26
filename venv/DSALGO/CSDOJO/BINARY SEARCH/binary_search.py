def search(arr, target):
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2 # make sure to round it down
        if arr[mid] == target:
	        return mid
        elif target < arr[mid]:
	        right = mid - 1
        else:
            left = mid + 1
    return -1

arr1 = [-2, 3, 4, 7, 8, 9, 11, 13]
assert search(arr1, 11) == 6
assert search(arr1, 13) == 7
assert search(arr1, -2) == 0
assert search(arr1, 8) == 4
assert search(arr1, 6) == -1
assert search(arr1, 14) == -1
assert search(arr1, -4) == -1
arr3 = [13,-2, 3, 4, 7, 8, 9, 11]
assert search(arr3,11)==7
arr4 = [8, 9, 11,13,-2, 3, 4, 7]
assert search(arr4,11)==2

arr2 = [3]
assert search(arr2, 6) == -1
assert search(arr2, 2) == -1
assert search(arr2, 3) == 0

print("If you didn't get an assertion error, this program has run successfully.")