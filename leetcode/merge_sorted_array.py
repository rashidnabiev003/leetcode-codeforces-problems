class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        sorted_array = []
        l = 0
        r = 0
        if m == 0 and n == 1:
            nums1[0] = nums2[0]
            return 
        elif len(nums1) == 1 and n == 0:
            return 
        while l < m or r < n:
            if r == n or l < m and nums1[l] < nums2[r]:
                sorted_array.append(nums1[l])
                l += 1
            else:
                sorted_array.append(nums2[r])
                r += 1

        for i in range(n + m):
            nums1[i] = sorted_array[i]