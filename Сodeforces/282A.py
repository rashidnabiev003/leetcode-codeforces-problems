n = int(input())
x = []
ans = 0
 
for i in range(n):
    b = input()
    if b == 'X++' or b == '++X':
        ans+=1
    elif b == 'X--' or b == '--X':
        ans-=1
 
print(ans)
