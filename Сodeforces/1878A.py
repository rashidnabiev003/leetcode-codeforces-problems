t = int(input())

def solve(numbers, n, k):
    if numbers.count(k) > 0:
        return "YES"
    return "NO"

for _ in range(t):
    n, k = map(int, input().split())
    numbers = list(map(int, input().split()))
    print(solve(numbers, n, k))