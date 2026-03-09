nums = [-23,3]
l = 2
r = 2
n = len(nums)
prefix = [0] * (n + 1)
    
for i in range(n):
    prefix[i + 1] = prefix[i] + nums[i]

min_sum = float('inf')

for i in range(n - l + 1):
    for j in range(i + l, min(i + r, n) + 1):
        current_sum = prefix[j] - prefix[i]
        if current_sum > 0:
            min_sum = min(min_sum, current_sum)

print( -1 if min_sum == float('inf') else min_sum)