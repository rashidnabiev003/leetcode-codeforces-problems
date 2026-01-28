#nums = [3,1,2,4]
nums = [0, 1]

r = len(nums) - 1
l = 0
extra = 0

while l <= r:
    if nums[l] % 2 == 0 and nums[r] % 2 == 0:
        l += 1
    elif nums[l] % 2 != 0 and nums[r] % 2 != 0:
        r -= 1
    elif nums[l] % 2 == 0 and nums[r] % 2 != 0:
        l += 1
        r -= 1
    else:
        extra = nums[l]
        nums[l] = nums[r]
        nums[r] = extra
        l += 1
        r -= 1
print(nums)
