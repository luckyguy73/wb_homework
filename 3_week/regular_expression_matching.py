class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl, pl = len(s) + 1, len(p) + 1
        dp = [[False] * pl for j in range(sl)]
        dp[0][0] = True

        for i in range(sl):
            for j in range(1, pl):
                dp[i][j] = dp[i][j - 2] or i > 0 and (s[i - 1] == p[j - 2] or p[j - 2] == '.') and dp[i - 1][j] if \
                    p[j - 1] == '*' else i > 0 and dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')

        return dp[-1][-1]
