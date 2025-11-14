n = int(input())

def is_sorted(array, array_lenght):
    for i in range(1, array_lenght):
        if array[i] < array[i - 1]:
            return False
    return True
        
for _ in range(n):
    a, b = map(int, input().split())
    array = list(map(int, input().split()))
    if a > 2 and b >= 2 or is_sorted(array, a) or a == b:
        print('YES')
    else:
        print("NO")