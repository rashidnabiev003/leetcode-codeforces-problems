s = "leetcode"
k = 2

vowels = {'a', 'e', 'i', 'o','u'}
count = 0
max_count = 0
l = 0
r = 0
while r < k:
    if s[r] in vowels:
        count += 1
    r += 1

max_count = count
r = k - 1
while r + 1 < len(s):
    r += 1
    l_prev = l
    l += 1
    if s[r] in vowels:
        count += 1
    if s[l_prev] in vowels:
        count -= 1
    max_count = max(count, max_count)

print(max_count)