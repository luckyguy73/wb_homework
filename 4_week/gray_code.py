class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = [0]
        for i in range(n):
            res += [x | (1 << i) for x in res[::-1]]
        return res
