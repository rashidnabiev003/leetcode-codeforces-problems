m = input()
n = input()
 
m = m.lower()
n = n.lower()
 
for i in range(len(n)):
    if m[i] > n[i]:
        print('1')
        break
    elif m[i] < n[i]:
        print('-1')
        break
else:
    print('0')