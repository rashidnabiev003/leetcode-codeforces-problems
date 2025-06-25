n = int(input())
sum = 0

if n % 2 == 0:
    sum = n // 2
else:
    sum = -1 * (n + 1)//2

print(sum)