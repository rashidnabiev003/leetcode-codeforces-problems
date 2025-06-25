b = input()
a = input()
c = []

b = list(str(b))
a = list(str(a))

for i in range(len(a)):
    if a[i] == b[i]:
        c.append(0)
    else:
        c.append(1)

print(*c, sep="")