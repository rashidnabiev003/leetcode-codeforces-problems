n = int(input())
cor = []
for i in range(n):
    b = list(map(int, input().split()))
    cor.append(b)

ans_x = 0
ans_y = 0
ans_z = 0

for i in range(n):
    ans_x += cor[i][0]
    ans_y += cor[i][1]
    ans_z += cor[i][2]

ans = ans_y + ans_x + ans_z
if ans == 0 and ans_z == 0 and ans_y == 0 and ans_x ==0:
    print('YES')
else:
    print('NO')
