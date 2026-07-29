nums = [1,1,1]

flag = False
l = 0
r = 0
count = 0
max_count = 0

while r < len(nums):
    if nums[r] == 0 and flag == False:
        flag = True
        r += 1
    elif nums[r] == 0 and flag == True:
        if nums[l] == 0:
            flag = False
        l += 1
    elif nums[r] == 1:
        r +=1

    max_count = max(max_count, r-l-1)

print(max_count)