n = int(input())

def solve(array, array_len):
    l = 0
    r = array_len - 1
    max_count = 0
    array = sorted(array)
    while l <= r:
        max_count += (array[r] - array[l])
        r -= 1
        l += 1
    return max_count

for _ in range(n):
    array_len = int(input())
    array = list(map(int, input().split()))
    print(solve(array, array_len))
