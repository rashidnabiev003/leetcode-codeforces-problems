nums = [1, 0, 1, 0, 1]
goal = 2

prefix_sum = 0
count = {0: 1}  
answer = 0

for num in nums:
    prefix_sum += num
    
    if prefix_sum - goal in count:
        answer += count[prefix_sum - goal]
    
    count[prefix_sum] = count.get(prefix_sum, 0) + 1

print(answer)