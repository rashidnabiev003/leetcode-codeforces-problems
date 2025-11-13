n = int(input())

def solve(a, b, c):
    if a < b < c:
        return "STAIR"
    elif a < b > c:
        return "PEAK"
    else:
        return "NONE"

for _ in range(n):
    a, b, c = map(int, input().split())
    print(solve(a, b, c))

