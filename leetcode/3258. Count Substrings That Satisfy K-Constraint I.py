s = "0011"
k = 1
n = len(s)
cnts = {'0': 0, '1': 0}
i = 0
ans = 0

for j in range(n):
    cnts[s[j]] += 1
    
    while cnts['0'] > k and cnts['1'] > k and i <= j:
        cnts[s[i]] -= 1
        i += 1
    
    ans += j - i + 1
    
print(ans)