nums1 = [1,2,3]
nums2 = [2,4,6]
hash_map1 = {x for x in set(nums1)}
hash_map2 = {x for x in set(nums2)}

m = [[x for x in hash_map1 if x not in hash_map2], [x for x in hash_map2  if x not in hash_map1]]
print(m)