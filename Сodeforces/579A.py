n = int(input())
b = list(bin(n))[2:]
sm = 0
for i in range(len(b)):
    sm += int(b[i])
print(sm)