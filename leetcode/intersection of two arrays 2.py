nums1 = [2,2]
nums2 = [1,2,2,1]
end_array = []
dictionary = {}

for i in range(len(nums2)):
    if dictionary.get(nums2[i]) is None:
        dictionary[nums2[i]] = 1
    else:
        dictionary[nums2[i]] += 1

for i in range(len(nums1)):
    if dictionary.get(nums1[i]) and dictionary[nums1[i]] > 0:
        end_array.append(nums1[i])
        dictionary[nums1[i]] -= 1

print(end_array)
