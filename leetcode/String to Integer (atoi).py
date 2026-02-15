s = "42"
s = s.lstrip()
i = 0
sing = 1


if s[0] == '-':
    i += 1
    sing = -1
elif s[0] == '+':
    i += 1

parsed = 0

while i < len(s):
    current = s[i]
    if not current.isdigit():
        break
    else:
        parser = parsed * 10 + int(current)

    i += 1

if parsed > 2 ** 31 - 1:
    print( 2 ** 31 - 1)
elif parsed < - 2 ** 31:
    print(-  2 ** 31)
else:
    print(parsed)

