from typing import List

list_of_num = list(map(int, input().split()))
target = int(input())

def twoSum(nums: List[int], target: int) -> List[int]:
    dict = {}
    for i in range(len(nums)):
        if dict.get(target - nums[i]) is None:
            dict[nums[i]] = i
        else:
            return dict.get(target- nums[i]), i
    return []
print(twoSum(list_of_num, target=target))