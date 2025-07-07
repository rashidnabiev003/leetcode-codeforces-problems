n = int(input())
ls = list(map(int, input().split()))
max_number = max(ls)
ans = 0

for i in range(len(ls)):
    ans += max_number - ls[i]

print(ans)