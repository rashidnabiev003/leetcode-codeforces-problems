n, m , a, b = map(int, input().split())

if b / m < a:
    y = n // m
    z = n - m * y
    print(min(a * z, b) + b * y)
else:
    print(n * a)