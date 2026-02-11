s = "anagram"
t = "nagarams"

if len(s) != len(t):
    #return False
    pass
dictionary = {}
for i in s:
    if dictionary.get(i) is None:
        dictionary[i] = 1
    else:
        dictionary[i] += 1

for i in t:
    if dictionary.get(i) is None or dictionary[i] == 0:
        print(False)
    else:
        dictionary[i] -= 1

print(True)
## best solution
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        for i in set(s):
            if s.count(i)!=t.count(i):
                return False
            
        return True