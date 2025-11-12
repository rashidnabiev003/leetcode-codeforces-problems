input_count = int(input())

def find_longest(list_len, array):
    max_zeros = 0
    zeros_count = 0
    for i in range(list_len):
        if array[i] == 0:
            zeros_count += 1
        else:
            max_zeros =  max(max_zeros, zeros_count)
            zeros_count = 0
        
    return max(max_zeros, zeros_count)

for _ in range(input_count):
    list_len = int(input())
    array = list(map(int, input().split()))
    print(find_longest(list_len, array))