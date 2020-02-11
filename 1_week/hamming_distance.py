class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return sum([1 for i in bin(x ^ y) if i == '1'])
        # return bin(x ^ y).count('1')
