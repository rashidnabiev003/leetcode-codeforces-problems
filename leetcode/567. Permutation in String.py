s1 = "ab"
s2 = "eidbaooo"

if len(s1) > len(s2):
    print(False)

s1_count = {}
for c in s1:
    s1_count[c] = s1_count.get(c, 0) + 1

window_count = {}
window_size = len(s1)

for i in range(len(s2)):
    window_count[s2[i]] = window_count.get(s2[i], 0) + 1
    
    if i >= window_size:
        left_char = s2[i - window_size]
        window_count[left_char] -= 1
        if window_count[left_char] == 0:
            del window_count[left_char]
    
    if i >= window_size - 1:
        if window_count == s1_count:
            print(True)
print(False)