a, b = map(int, input().split())
array = []
array.append(2)

for i in range(3, 50, 2):
    flag = False
    for j in range(2, i):
        if i % j == 0 and i != j:
            flag = True
    if flag == False:
        array.append(i)
try:
    if array[array.index(a) + 1] == b:
        print("YES")
    else:
        print("NO")
except:
    print("NO") 