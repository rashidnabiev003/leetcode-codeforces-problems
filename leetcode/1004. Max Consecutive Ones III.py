nums = [1,1,1,0,0,0,1,1,1,1,0]
k = 2
dictionary = {1:0, 0: 1}
ans = 0
l = 0
for r in range(len(nums)):
    dictionary[nums[r]] += 1
    if (r - l + 1) - dictionary[1] <= k:
        ans = max(ans, (r - l + 1))
    else:
        dictionary[nums[l]] -= 1
        l += 1

print(ans)