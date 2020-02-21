class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        s = pattern
        t = string.split()
        return len(set(zip(s, t))) == len(set(s)) == len(set(t)) and len(s) == len(t)
