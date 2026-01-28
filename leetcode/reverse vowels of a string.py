vowels = {'a', 'e', 'i', 'o', 'u', 'A' , 'E', 'I', 'O', 'U'}
s = 'IceCreAm'
s = list(s)

r = len(s) - 1
l = 0
while l <= r:
    if s[l] in vowels and s[r] in vowels:
        extra = s[l]
        s[l] = s[r]
        s[r] = extra
        l += 1
        r -= 1
    elif s[l] in vowels and s[r] not in vowels:
        r -= 1
    elif s[r]in vowels and s[l] not in vowels:
        l += 1
    else:
        r -= 1
        l += 1

print(''.join(filter(str, s)))