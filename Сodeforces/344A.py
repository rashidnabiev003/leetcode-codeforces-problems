n = int(input())
sm = 1
flag = input()
for i in range(1, n):
    b = input()
    if flag != b:
        sm += 1
        flag = b

print(sm)