class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        possible_sums = {0}
        for n in nums:
            possible_sums.update({(v + n) for v in possible_sums})
        return (sum(nums) / 2) in possible_sums
