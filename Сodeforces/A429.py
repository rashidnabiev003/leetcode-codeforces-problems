a = int(input())
b = int(input())
c = int(input())
max_num = 0

if a + b + c > max_num:
    max_num = a + b + c
if a * b * c > max_num:
    max_num = a * b * c
if (a + b) * c > max_num:
    max_num = (a + b) * c
if a * (b + c) > max_num:
    max_num = a * (b + c)

print(max_num)

