nums1 = [4,1,2]
nums2 = [1,3,4,2]
answer = []
stack = []
hash_map = {}

for i in nums2:
    while stack and i > stack[-1]:
        prev = stack.pop()
        hash_map[prev] = i
    stack.append(i)

for i in nums1:
    answer.append(hash_map.get(i, - 1))

print(answer)
