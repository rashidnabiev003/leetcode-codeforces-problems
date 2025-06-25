n, b = map(int, input().split())
c = 0

if n // 2 > b or n // 2 == b:
    c = 2 * (b - 1) + 1
    print(c)
elif n // 2 < b and n % 2 == 0:
    c = 2 * (b - n // 2)
    print(c)
elif n // 2 < b and n % 2 != 0:
    c = 2 * (b - n // 2 - 1)
    if c == 0:
        print(n)
    else:
        print(c)
elif n // 2 == b and n % 2 == 0:
    print(n - 1)