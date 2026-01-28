nums = [-1]
n = len(nums)
sorted_nums = [x*0 for x in range(n)]
l = 0
r = n - 1
position = r

while l <= r and position >= 0:
    left_sq = nums[l] ** 2
    right_sq = nums[r] ** 2
    if left_sq > right_sq:
        sorted_nums[position] = left_sq
        l += 1
    else:
        sorted_nums[position] = right_sq
        r -= 1
    position -= 1

print(sorted_nums)
