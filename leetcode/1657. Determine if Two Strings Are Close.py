word1 = "aaabbbbccddeeeeefffff"
word2 = "aaaaabbcccdddeeeeffff"

from collections import Counter

word1_count = Counter(word1)
word2_count = Counter(word2)

a = []
b = []

for i, j in zip(word1_count.values(), word2_count.values()):
    a.append(i)
    b.append(j)

print(sorted(a) == sorted(b) and set(word1) == set(word2))