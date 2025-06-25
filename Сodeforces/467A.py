n = int(input())
x = []
sum = 0

for i in range(n):
    x.append(list(map(int, input().split())))
    if (x[i][1] - x[i][0])  >= 2:
        sum += 1

print(sum)
