n = input()
x = ['h', 'e', 'l', 'l', 'o']
res = 0

n = list(n)

for i in range(len(n)):
    if n[i] == x[res]:
        res += 1
    if res == 5:
        break

if res == 5:
    print('YES')
else:
    print('NO')