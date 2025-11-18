nums = [0,1,2,2,3,0,4,2]
val = 2

def removeElement(nums, val) -> int:
    for i in range(len(nums) - 1):
        if nums[i] == val:
            nums.pop(i)
    return len(nums)

print(removeElement(nums, val))
nums.reverse()