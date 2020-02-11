class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(l for l in s.lower() if l.isalnum())
        return s == s[::-1]
