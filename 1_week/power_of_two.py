class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return 0 < n == (n & -n)
        # return n > 0 and (n & (n - 1)) == 0
