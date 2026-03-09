s = "AABABBA"
k = 1
unique = set(s)
dictionary = {key: 0 for key in unique}
l = 0
r = 0
ans = 0

for r in range(len(s)):
    dictionary[s[r]] += 1
    max_value = 0
    for key, value in dictionary.items():
        max_value = max(max_value, value)
    if (r - l + 1) - max_value <= k:
        ans = max(ans, r - l + 1)
    else:
        dictionary[s[l]] -= 1
        l += 1
    
print(ans)
    
