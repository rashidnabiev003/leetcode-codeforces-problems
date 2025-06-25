b = input()
x = []
 
for i in range(len(b)):
    if i%2 != 1 or i == 0:
        x.append(int(b[i]))
 
b = []
x.sort()
 
for i in range(len(x)):
    b.append(x[i])
    if i < len(x)-1:
        b.append('+')
 
print(*b,sep='')