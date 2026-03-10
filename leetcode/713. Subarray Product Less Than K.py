nums = [10,5,2,6]
k = 100

left = 0
answer = 0
product = 1

for right in range(len(nums)):
    product *= nums[right]

    while product >= k and left <= right:
        product //= nums[left]
        left += 1

    answer += right - left + 1
    
print(answer)
