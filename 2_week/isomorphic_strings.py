class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # 28ms faster than 97.69%
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            elif t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
        return True

        # 40 ms faster than 56.31%
        # dst, dts = dict(zip(s, t)), dict(zip(t, s))
        # for i, c in enumerate(s):
        #     if dst[c] != t[i] or dts[t[i]] != c: return False
        # return True

        # 32 ms faster than 92.62%
        # s, t = str(s), str(t)
        # table1 = str.maketrans(s, t)
        # table2 = str.maketrans(t, s)
        # return s.translate(table1) == t and t.translate(table2) == s