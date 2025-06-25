n = int(input())
x = list(map(int, input().split()))

x.sort(reverse=True)

for i in range(n):
    if len(x) == 2:
        if x[0] == x[1]:
            print(2)
            break
        else:
            print(1)
            break
    elif len(x) == 1:
        print(1)
        break
    elif sum(x[0:i]) > sum(x[i:]):
        print(len(x[:i]))
        break