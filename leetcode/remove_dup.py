#nums = [0,0,1,1,1,2,2,3,3,4]
nums = [1,1,2]
def removeDuplicates(nums) -> int:
        sorted_dedup = []
        l = 0
        r = 0
        while l <= len(nums) - 1 and r <= len(nums) - 1:
            if l == r:
                sorted_dedup.append(nums[l])
                r += 1
            elif nums[l] == nums[r] and l != r:
                r += 1
            elif nums[l] != nums[r]:
                l = r
        
        return sorted_dedup

print(removeDuplicates(nums))