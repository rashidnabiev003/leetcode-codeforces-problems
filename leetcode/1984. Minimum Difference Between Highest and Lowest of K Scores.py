nums = [87063,61094,44530,21297,95857,93551,9918]
k = 6
if len(nums) == 1 or k == 1:
    print(0)
nums = sorted(nums)
min_diff = float('inf')

for i in range(len(nums) - k + 1):
    min_diff = min(min_diff, nums[i + k - 1] - nums[i])

print(min_diff)