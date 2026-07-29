height = [1,1]
l = 0
r = len(height) - 1
count = 0
max_count = 0

while l <= r:
    count = min(height[l], height[r]) * (r - l)
    max_count = max(max_count, count)
    if height[r] < height[l]:
        r -= 1
    elif height[r] == height[l]:
        r -= 1
        l += 1
    else:
        l += 1

print(max_count)