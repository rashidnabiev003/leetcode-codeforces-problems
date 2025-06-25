n = list(input())
b = n.count('4')
a = n.count('7')
if (a + b) == 4 or (a + b) == 7:
    print('YES')
else:
    print('NO')