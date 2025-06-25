n = int(input())

def unic(sn):
    v = str(sn)
    b = list(v)
    for i in range(4):
        c = b.count(b[i])
        if c > 1:
            return True
        else:
            c = 0

n += 1
while True:
    if unic(n):
        n += 1
    else:
        print(n)
        break







