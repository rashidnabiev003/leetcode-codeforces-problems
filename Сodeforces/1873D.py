n = int(input())

def solve(array, array_len, window_len):
    if 'B' not in array:
        return 0
    elif array_len == window_len:
        return 1
    
    max_count = 0

    for i in range(array_len):
        if array[i] == 'B':
            if i + window_len > array_len:
                for j in range(i, array_len):
                    if array[j] == 'B':
                        return max_count + 1
                    else:
                        return max_count
            elif i + window_len <= array_len:
                for j in range(i, i + window_len):
                    array[j] = 'W'
            i += window_len
            max_count += 1
    
    return max_count

for _ in range(n):
    array_len, window_len = map(int, input().split())
    array = list(map(str, input().strip()))
    print(solve(array, array_len, window_len))