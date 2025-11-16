n = int(input())

def solve(array_len, array):
    test_array = [0 for x in range(array_len)]
    l = 0
    r = array_len - 1
    pointer = 0
    while l <= r and pointer <= array_len:
        if pointer % 2 == 0:
            test_array[pointer] = array[l]
            l += 1
        else:
            test_array[pointer] = array[r]
            r-= 1
        pointer += 1
    return test_array[0:array_len]

for i in range(n):
    array_len = int(input())
    array = list(map( int, input().split()))
    print(*solve(array=array, array_len=array_len))