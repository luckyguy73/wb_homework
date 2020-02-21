class Solution:
    def firstUniqChar(self, s: str) -> int:
        cache = {}
        for idx in range(len(s)):
            if s[idx] not in cache:
                if s.count(s[idx], idx) == 1:
                    return idx
                else:
                    cache[s[idx]] = 1
        return -1
