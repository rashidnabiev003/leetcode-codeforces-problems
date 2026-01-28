class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)
        l = 0
        r = 0
        if len(s) > len(t):
            return False
            
        while l <= len(s) - 1:
            if r > len(t) - 1:
                return False
                break
            if s[l] == t[r]:
                l += 1
                r +=1
            else:
                r += 1
        return True