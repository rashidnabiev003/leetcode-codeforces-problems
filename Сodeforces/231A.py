a = int(input())
x = []
 
for i in range(a):
    b = list(map(int, input().split()))
    x.append(b)
ans = 0
cur = 0
for i in range(a):
    for j in range(3):
        if x[i][j] == 1:
            cur+=1
    if cur >= 2:
        ans+=1
    cur = 0
print(ans)