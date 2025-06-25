n, h = map(int, input().split())
x = list(map(int, input().split()))
res = n

for i in range(len(x)):
    if x[i] > h:
        res += 1

print(res)