s = ["h","e","l","l","o"]

l = 0
extra = 0
r = len(s) - 1

while l <= r:
    extra = s[l]
    s[l] = s[r]
    s[r] = extra
    l += 1
    r -= 1

print(s)
