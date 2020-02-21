from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # Solution 3
        duplicate = sum(nums) - sum(set(nums))
        missing = int((len(nums) * (len(nums) + 1)) / 2) - sum(set(nums))
        return [duplicate, missing]

        # Solution 1
        # from collections import Counter
        # nums_count = Counter(nums)
        # nums_range = list(range(1, max(nums_count.keys()) + 1))
        # duplicate = Counter(nums).most_common()[0][0]
        # missing = [x for x in nums_range if x not in nums]
        # if not missing: missing = [nums_range[-1] + 1]
        # return [duplicate, *missing]

        # Solution 2
        # seen, duplicate, minimum, maximum = set(), 0, nums[0], nums[0]
        # for n in nums:
        #     if n < minimum:
        #         minimum = n
        #     if n > maximum:
        #         maximum = n
        #     if n in seen:
        #         duplicate = n
        #     else:
        #         seen.add(n)
        # missing, nums_range = 0, list(range(1, maximum + 1))
        # for num in nums_range:
        #     if num not in nums:
        #         missing = num
        # if not missing: missing = nums_range[-1] + 1
        # return [duplicate, missing]
