class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        result = 0
        for letter in s + t:
            result ^= ord(letter)
        return chr(result)
