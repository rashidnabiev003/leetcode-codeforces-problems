from collections import Counter

arr = [1,2]
col = Counter(arr) 
d = dict(col)
del col
col = {}

for i in d.values():
    if i not in col:
        col[i] = 0

print(len(col) == len(set(arr)) )