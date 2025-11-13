n = int(input())

def solve(length, arr):
    l = 0
    r = length - 1
    while l < r:
        if arr[l] == arr[r]:
            return (r - l) + 1 if (r - l) > 0 else 0
        else:
            r -= 1
            l += 1
    else:
        if l > r:
            return 0
        return 1

for _ in range(n):
    array_len = int(input())
    binary_array = list(map(int, input()))
    print(solve(array_len, binary_array))