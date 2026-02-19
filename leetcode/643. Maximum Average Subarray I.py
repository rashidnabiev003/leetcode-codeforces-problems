nums = [1,12,-5,-6,50,3]
k = 4
i = 0
j = k - 1
average = -float('inf')
summary = sum(nums[0:j])

while j < len(nums):
    summary += nums[j]
    average = max(average, summary / k)
    summary -= nums[i]
    i += 1
    j += 1

print(average)