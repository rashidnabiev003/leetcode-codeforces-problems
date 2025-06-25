n, t = map(int, input().split())
x = input()
x = list(x)
cnt = 0
if n != 1 :
    for i in range(t):
        for j in range(n):
            if cnt < n - 2:
                if x[cnt] == 'B' and x[cnt + 1] == 'G':
                    x[cnt] = 'G'
                    x[cnt + 1] = 'B'
                    cnt += 2
                else:
                    cnt += 1
            else:
                if x[-1] == 'G' and x[-2] == 'B':
                    x[-1] = 'B'
                    x[-2] = 'G'
        cnt = 0
else:
    print(*x, sep='')
if n != 1:
    print(*x,sep='')