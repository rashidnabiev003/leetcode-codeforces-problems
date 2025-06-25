n = list(input())
ans_1 = 0
ans_2 = 0
cur = 3
for i in range(len(n)):
    if n[i] == '1':
        ans_2 = 0
        ans_1 += 1
        cur = 1
        if ans_1 >= 7:
            print('YES')
            break

    elif n[i] == '0':
        ans_1 = 0
        ans_2 += 1
        cur = 0
        if ans_2 >= 7:
            print('YES')
            break
    if n[i] == 0:
        cur = 0

    else:
        cur = 1

if ans_2 < 7 and ans_1 < 7:
    print('NO')
