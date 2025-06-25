n = int(input())
x = []
ans = 0
maximum = 0

for i in range(n):
    b = list(map(int, input().split()))
    x.append(b)

for i in range(n):
    ans -= x[i][0]
    ans += x[i][1]
    if ans > maximum:
        maximum = ans

print(maximum)