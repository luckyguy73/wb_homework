class Solution:
    def twoSum(self, nums, target):
        d = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff not in d:
                d[v] = i
            else:
                return [d[diff], i]
