from typing import List


class Solution:
    def numSpecialEquivGroups(self, A: List[str]) -> int:
        func = lambda x: ''.join(sorted(x[::2]) + sorted(x[1::2]))
        return len(set(func(x) for x in A))
