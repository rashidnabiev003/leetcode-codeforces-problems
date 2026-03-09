nums = [1, 2, 3, 4]
ans = []
i = 1
curr_len = 0
while i <= len(nums) - 2:
    if nums[i] - nums[i - 1] == nums[i + 1] - nums[i]:
        curr_len += 1
    else:
        ans.append(curr_len)
        curr_len = 0
    i += 1
ans.append(curr_len)
answer = 0
def solve(curr_len):
    m = (curr_len + 2) - 3 + 1
    return (m * (m + 1) // 2)

for i in ans:
    answer += solve(i)

print(answer)