class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([l[::-1] for l in s.split()])
