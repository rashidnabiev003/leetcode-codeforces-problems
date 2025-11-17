n = int(input())

def solve(array, array_len):
    l = 0
    end_array = []
    r = l + 1
    while r <= array_len - 1:
        if array[l] != array[r]:
            r += 1
        elif array[l] == array[r]:
            end_array.append(array[l])
            l = r + 1
            r = l + 1
    return end_array

for _ in range(n):
    array_len = int(input())
    array = list(map(str, input().strip()))
    print(*solve(array, array_len), sep="") 