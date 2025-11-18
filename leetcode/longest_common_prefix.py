strs = ["flower","flow","flight"]
#strs = ["dog","racecar","car"]
#strs = ["flower","flower","flower","flower"]

def longestCommonPrefix(strs) -> str:
        s = ""
        r = 1
        prefix = ""
        while r <= len(strs[0]):
            prefix = strs[0][0:r]
            for string in strs:
                if prefix == string[0:r]:
                    continue
                else:
                    return s
            s = prefix
            r += 1
        return s

print(longestCommonPrefix(strs))