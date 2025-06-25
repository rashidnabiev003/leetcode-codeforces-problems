ans = input()
b = input()
b = list(b)
ans = list(reversed(ans))

if ans == b:
    print('YES')
else:
    print('NO')