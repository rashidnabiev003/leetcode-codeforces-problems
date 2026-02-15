s = "cbaebabacd"
p = "abc"
indexes = []

def is_anagram(str1, str2):
    if len(str1)!=len(str2):
        return False
    for i in set(str1):
        if str1.count(i)!=str2.count(i):
            return False  
    return True

right = len(p)

for i in range(0, len(s) - len(p) + 1):
    if is_anagram(s[i:i + right], p) is True:
        indexes.append(i)

print(indexes) 
#best solution 
def findAnagrams(s: str, p: str):
    if len(p) > len(s):
        return []
    
    target = [0] * 26
    window = [0] * 26
    result = []
    m = len(p)
    
    # Инициализация
    for ch in p:
        target[ord(ch) - ord('a')] += 1
    
    for i in range(len(s)):
        window[ord(s[i]) - ord('a')] += 1
        if i >= m:
            window[ord(s[i - m]) - ord('a')] -= 1
        if i >= m - 1 and window == target:
            result.append(i - m + 1)
    
    return result
