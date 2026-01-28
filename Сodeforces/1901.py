n = int(input())

def solve(len_array, last_point, array):
    max_range = array[0]
    if len_array > 1:
        for i in range(1, len_array):
            if array[i] - array[i - 1] > max_range:
                max_range = array[i] - array[i - 1]
        
        return max(max_range, (last_point - array[-1]) * 2)
    else:
        return max(array[0], (last_point - array[0]) * 2)

for i in range(n):
    len_array, last_point = map(int, input().split())
    array = list(map(int, input().split()))
    print(solve(len_array, last_point, array))
