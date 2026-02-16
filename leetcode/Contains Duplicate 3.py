nums = [1,0,1,1]
k = 1
dictionary = {}

l = 0
while l < len(nums):
    if nums[l] in dictionary and abs(dictionary[nums[l]] - l) <= k:
            print(True)
            break
    else:
        dictionary[nums[l]] = l
    l += 1
print(False)

# best 
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        if len(nums) == len(set(nums)):
            return False
        for i in range(len(nums)):
            if nums[i] in nums[i+1:k+i+1]:
                return True
        return False