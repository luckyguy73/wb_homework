class Solution:
    def rob(self, nums: List[int]) -> int:
        def _rob(nums: List[int]) -> int:
            rob = not_rob = 0
            for money in nums:
                rob, not_rob = not_rob + money, max(rob, not_rob)
            return max(rob, not_rob)

        if len(nums) == 1: return nums[0]
        return max(_rob(nums[:-1]), _rob(nums[1:]))
