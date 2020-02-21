import collections
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def make_subs():
            subs = [[] * 9 for _ in range(9)]
            for i in range(0, len(board), 3):
                for j in range(0, len(board), 3):
                    for x in range(3):
                        for y in range(3):
                            subs[j // 3 + i].append(board[x + i][y + j])
            return subs

        def check_area(area):
            for i in range(len(area)):
                for n in nums:
                    if area[i].count(n) > 1:
                        return False
            return True

        nums, cols, subs = '123456789', list(zip(*board)), make_subs()
        return all([check_area(x) for x in (board, cols, subs)])
