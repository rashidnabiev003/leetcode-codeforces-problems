target = 7
nums = [2,3,1,2,4,3]
left = 0
right = 0
current_sum = nums[0]
min_len = float('inf')

while left < len(nums) - 1 and right <= len(nums) - 1:
    if current_sum < target:
        right += 1
        if right == len(nums):
            break
        current_sum += nums[right]
    elif current_sum >= target:
        min_len = min(min_len, right - left + 1)
        current_sum -= nums[left]
        left += 1

print(0 if min_len == float('inf') else min_len)

#вариант читабельнее
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not nums:
            return 0
        
        left = 0
        current_sum = 0
        min_len = float('inf')
        
        for right in range(len(nums)):
            current_sum += nums[right]  # Расширяем окно
            
            # Сжимаем окно, пока сумма >= target
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)
                current_sum -= nums[left]
                left += 1
        
        return 0 if min_len == float('inf') else min_len
    
