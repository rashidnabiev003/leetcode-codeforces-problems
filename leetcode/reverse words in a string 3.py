class Solution:
    def reverseWords(self, s: str) -> str:
        s = ' '.join(map(lambda x: x[::-1], s.split(' ')))
        return s