strs = ["eat","tea","tan","ate","nat","bat"]
final = [[strs[0]]]

def is_anagram(str1, str2):
    if len(str1)!=len(str2):
        return False
    for i in set(str1):
        if str1.count(i)!=str2.count(i):
            return False  
    return True

pointer = 1
f_pointer = 0

while pointer <= len(strs) - 1:
    if is_anagram(final[f_pointer][0], strs[pointer]) is True:
        final[f_pointer].append(strs[pointer])
        pointer += 1
        f_pointer = 0
    elif f_pointer < len(final) - 1:
        f_pointer += 1
    else:
        final.append([strs[pointer]])
        f_pointer = 0
        pointer += 1

print(final)

#best
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        from collections import defaultdict
        def groupAnagrams(strs):
            groups = defaultdict(list)
            for s in strs:
                key = ''.join(sorted(s))  
                groups[key].append(s)
            return list(groups.values())
        return groupAnagrams(strs)