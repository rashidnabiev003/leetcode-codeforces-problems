nums = [2,1,-1]
prefix_sum = [0]

for i in range(len(nums)):
    prefix_sum.append(prefix_sum[i] + nums[i])

for i in range(1, len(prefix_sum)):
    if prefix_sum[i - 1] == prefix_sum[-1] - prefix_sum[i]:
        print(i - 1)
        break

print(-1)