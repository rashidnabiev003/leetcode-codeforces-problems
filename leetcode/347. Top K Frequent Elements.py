from collections import Counter
nums = [1,1,1,2,2,3, 4, 4, 5, 6]
k = 2
d = Counter(nums)
cur = d[nums[0]]
max_key = 0
max_key_num = 0
ans = []
for s in range(k):
    for i, j in d.items():
        if j > max_key_num:
            max_key = i
            max_key_num = j
    max_key_num = 0
    del d[max_key]
    ans.append(max_key)

print(ans)
    
