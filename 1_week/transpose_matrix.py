class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        return [[col for col in row] for row in zip(*A)]
