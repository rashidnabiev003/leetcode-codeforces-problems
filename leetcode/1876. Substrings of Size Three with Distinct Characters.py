s = "aababcabc"
seq_count = 0
i = 0
j = 3

while j <= len(s):
    if len(set(s[i:j])) == 3:
        seq_count += 1
    i += 1
    j += 1

print(seq_count)