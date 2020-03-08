from functools import reduce


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        back = lambda res, c: res[:-1] if c == '#' else res + c
        return reduce(back, S, "") == reduce(back, T, "")
