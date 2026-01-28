s = "ab-cd"
s= list(s)
l = 0
r = len(s) - 1
while l <= r:
    if s[l].isalpha() == False:
        l += 1
    elif s[r].isalpha() == False:
        r -= 1
    else:
        s[l], s[r] = s[r], s[l]
        r -= 1
        l += 1
print(''.join(map(str, s)))
