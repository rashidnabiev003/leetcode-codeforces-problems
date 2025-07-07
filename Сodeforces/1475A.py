n = int(input())

for _ in range(n):
    ans = int(input())
    while ans > 1:
        if ans % 2 == 0:
            ans = ans // 2
        else:
            print("YES")
            break
    else:
        print("NO")