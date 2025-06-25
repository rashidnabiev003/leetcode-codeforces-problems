n = int(input())
b = list(map(int, input().split()))

if b.count(1) == 0:
    print('easy')
else:
    print('hard')