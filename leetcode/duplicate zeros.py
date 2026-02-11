arr = [1,0,2,3,0,4,5,0]
zeros = arr.count(0)
n = len(arr)

i = n - 1
j = n - 1 + zeros

while i >= 0:
    if arr[i] != 0:
        if j < n:
            arr[j] = arr[i]
        j -= 1
    else:
        if j < n:
            arr[j] = 0
        j -= 1
        if j < n:
            arr[j] = 0
        j -= 1
    i -= 1

print(arr)