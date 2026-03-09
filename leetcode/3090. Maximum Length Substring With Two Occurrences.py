s = "aaaa"
dictionary  =  {}
l = 0
r = 0
max_string_len = 0
while r < len(s):
    if s[r] not in dictionary:
        dictionary[s[r]] = 1
    else:
        if dictionary[s[r]] < 2:
            dictionary[s[r]] += 1
        else:
            max_string_len = max(max_string_len, len(s[l:r]))
            dictionary[s[r]] += 1
            while dictionary[s[r]] > 2:
                dictionary[s[l]] -= 1
                l += 1
    r += 1
    max_string_len = max(max_string_len, len(s[l:r]))
    
print(max_string_len)