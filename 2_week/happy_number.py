class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s and n != 1:
            s.add(n)
            n = sum((int(x) ** 2 for x in str(n)))
        return n == 1
