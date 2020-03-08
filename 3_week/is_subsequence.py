class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        start = end = 0
        m, n = len(s), len(t)
        while start < m:
            if end >= n: return False
            if s[start] == t[end]: start += 1
            end += 1
        return True
