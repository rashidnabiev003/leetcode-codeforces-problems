def longestAlternatingSubarray(nums: list[int], threshold: int) -> int:
    max_len = 0
    i = 0
    
    while i < len(nums):
        if nums[i] % 2 != 0 or nums[i] > threshold:
            i += 1
            continue
        
        j = i
        while j < len(nums) and nums[j] <= threshold:
            if j > i and nums[j] % 2 == nums[j-1] % 2:
                break
            j += 1
        
        max_len = max(max_len, j - i)
        i = j if j > i else i + 1
    
    return max_len


print(longestAlternatingSubarray(nums = [2,8], threshold = 4))