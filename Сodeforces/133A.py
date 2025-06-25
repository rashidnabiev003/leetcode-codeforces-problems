b = input()
b = list(str(b))
c = ['H', 'Q', '9']
asm = 0


for i in range(len(c)):
    for j in range(len(b)):
        if c[i] == b[j]:
            asm += 1

    if asm > 0:
        print("YES")
        break

if asm == 0:
    print('NO')
