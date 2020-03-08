class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ret = [[]]
        for n in nums:
            ret += [r + [n] for r in ret]
        return ret

