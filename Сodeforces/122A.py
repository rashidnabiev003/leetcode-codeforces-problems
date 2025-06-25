n = int(input())


def is_happy(arg):
    n = list(str(arg))
    for i in range(len(n)):
        if n[i] != '4' and n[i] != '7':
            return False
    else:
        return True


for i in range(4, n + 1):
    if is_happy(i):
        if n % i == 0:
            print('YES')
            break
else:
    print('NO')