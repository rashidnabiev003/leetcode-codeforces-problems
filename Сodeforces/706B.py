n = int(input())
magaz = list(map(int, input().split()))
q = int(input())
magaz.sort()

def binary_search(arr, x):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            result = mid
            low = mid + 1
        else:
            high = mid - 1
    return result + 1 if result != -1 else 0

for _ in range(q):
    money = int(input())
    print(binary_search(magaz, money))