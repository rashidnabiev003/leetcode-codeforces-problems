n = int(input())
x = []

for i in range(n):
    x.append(list(map(int, input().split())))

for i in range(n):
    if x[i][0] % x[i][1] == 0:
        print(0)
    elif x[i][0] > x[i][1]:
        print(x[i][1] - (x[i][0] % x[i][1]))
    elif x[i][0] < x[i][1]:
        print(x[i][1] - x[i][0])


