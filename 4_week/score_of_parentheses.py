class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        res, i = [0] * 30, 0
        for c in S:
            i += 1 if c == '(' else -1
            res[i] = res[i] + max(res[i + 1] * 2, 1) if c == ')' else 0
        return res[0]

