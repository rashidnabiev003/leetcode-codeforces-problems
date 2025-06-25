a = int(input())
x = []
 
for i in range(a):
    b = input()
    x.append(b)
 
 
for i in range(a):
    if len(x[i]) > 10 :
        print(x[i][0], len(x[i])-2, x[i][-1],sep='')
    else:
        print(x[i],sep='')