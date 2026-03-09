s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
dictionary = {}
ans = []
for i in range(len(s) - 10):
    if s[i:i+10] not in dictionary :
        dictionary[s[i:i+10]] = 1
    else:
        dictionary[s[i:i+10]] += 1

for i, j in dictionary.items():
    if j > 1:
        ans.append(i)

print(ans)