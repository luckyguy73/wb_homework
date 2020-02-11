class Solution:
    def findComplement(self, num: int) -> int:
        bits = len(bin(num)) - 2
        mask = 2 ** bits - 1
        return num ^ mask
