class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum((1 for x in S if x in J))
