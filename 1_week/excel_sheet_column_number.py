class Solution:
    def titleToNumber(self, s: str) -> int:
        return sum([(ord(c) - 64) * (26 ** x) for x, c in enumerate(s[::-1])])
