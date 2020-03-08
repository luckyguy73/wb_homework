class Solution:
    def myPow(self, x: float, n: int, memo={}) -> float:
        if n < 0:
            x, n = 1 / x, -n
        result = 1
        while n:
            if n & 1: result *= x
            x *= x
            n >>= 1
        return result
