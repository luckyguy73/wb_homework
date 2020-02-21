from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Solution 3
        string = [s[:len(p)].count(c) for c in [chr(x) for x in range(ord('a'), ord('z') + 1)]]
        anagrams = [p.count(c) for c in [chr(x) for x in range(ord('a'), ord('z') + 1)]]
        if string == anagrams: yield 0
        for i, c in enumerate(s[len(p):]):
            string[ord(s[i]) - ord('a')] -= 1
            string[ord(c) - ord('a')] += 1
            if string == anagrams:
                yield i + 1

        # Solution 4
        # check, dp, lp = {}, {x: p.count(x) for x in list(p)}, len(p) - 1
        # for i in range(len(s)):
        #     check[s[i]] = check.setdefault(s[i], 0) + 1
        #     if i >= lp:
        #         if check == dp:
        #             yield i - lp
        #         check[s[i - lp]] = check.setdefault(s[i - lp], 0) - 1
        #         if check.get(s[i - lp]) == 0: del check[s[i - lp]]

        # Solution 2
        # ans, list_s, list_p, lp = [], [], sorted(list(p)), len(p) - 1
        # for i in range(len(s)):
        #     list_s.append(s[i])
        #     list_s.sort()
        #     if i >= lp:
        #         if list_s == list_p:
        #             ans.append(i - lp)
        #         list_s.remove(s[i - lp])
        # return ans

        # Solution 1
#         from collections import Counter
#         ls, lp, results = len(s), len(p), []
#         dic_s, dic_p = Counter(s[:lp - 1]), Counter(p)
#         for i in range(lp - 1, ls):
#             first = i - (lp - 1)
#             dic_s[s[i]] = dic_s.setdefault(s[i], 0) + 1
#             if dic_s == dic_p:
#                 results.append(first)
#             if dic_s[s[first]] > 1:
#                 dic_s[s[first]] -= 1
#             else:
#                 del dic_s[s[first]]

#         return results