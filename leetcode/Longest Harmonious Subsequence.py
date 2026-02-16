from collections import defaultdict

nums = [1,2,3,4]
max_subsequence = 0

dictionary = defaultdict(int)
for i in nums:
    dictionary[i] += 1

for i in dictionary:
    if dictionary.get(i + 1) is not None:
        max_subsequence = max(dictionary[i + 1] + dictionary[i], max_subsequence)

print(dictionary)
print(max_subsequence)
