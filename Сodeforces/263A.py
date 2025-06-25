x = []
ans = 0
a = 0
b = 0
 
for i in range(5):
    b = list(map(int, input().split()))
    x.append(b)
 
for i in range(5):
    for j in range(5):
        if x[i][j] == 1:
            a = i
            b = j
 
print((abs(a-2))+abs(b-2))