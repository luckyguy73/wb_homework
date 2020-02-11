class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        rev = s[::-1]
        s.clear()
        s.extend(rev)
