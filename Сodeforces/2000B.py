n = int(input())
 
def solve(array_len, array):
    dictionary = {}
    dictionary[array[0]] = True
    for i in range(1, array_len):
        if dictionary.get(array[i] - 1) or dictionary.get(array[i] + 1):
            dictionary[array[i]] = True
        else:
            return 'NO'
    return 'YES'
   
 
for _ in range(n):
    array_len = int(input())
    array = list(map(int, input().split()))
    print(solve(array_len, array))