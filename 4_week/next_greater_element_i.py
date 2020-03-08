class Solution:
    def nextGreaterElement(self, findNums, nums):
        return [next((y for y in nums[nums.index(x):] if y > x), -1) for x in findNums]
