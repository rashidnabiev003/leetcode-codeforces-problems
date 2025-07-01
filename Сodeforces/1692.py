n = int(input())

def calculate(l:list):
    total = 0
    for i in range(1, 4):
        if l[i] > l[0]:
            total+=1
    return  total

for i in range(n):
    runners = list(map(int, input().split()))
    print(calculate(runners))