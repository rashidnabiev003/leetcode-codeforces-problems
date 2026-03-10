def findClosestElements(arr, k, x):
    left, right = 0, len(arr) - k
    
    while left < right:
        mid = (left + right) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    
    return arr[left:left + k]

arr = [1,1,1,10,10,10]
k = 1
x = 9
print(findClosestElements(arr, k, x))