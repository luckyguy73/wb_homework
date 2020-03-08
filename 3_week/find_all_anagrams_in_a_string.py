class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        idx, rng = len(p) - 1, range(ord('a'), ord('z') + 1)
        text = {c: s[:idx].count(c) for c in [chr(x) for x in rng]}
        anagrams = {c: p.count(c) for c in [chr(x) for x in rng]}
        for i, val in enumerate(s[idx:]):
            text[val] += 1
            if text == anagrams: yield i
            text[s[i]] -= 1

        # Solution 3
        # from collections import Counter
        # ans, ana_counter, str_counter = [], Counter(p), Counter(s[:len(p) - 1])
        # for idx, val in enumerate(s[len(p) - 1:]):
        #     str_counter[val] = str_counter.setdefault(val, 0) + 1
        #     if ana_counter == str_counter:
        #         ans.append(idx)
        #     str_counter[s[idx]] -= 1
        #     str_counter += Counter()
        # return ans

        # Solution 4
#         check, dp, lp = {}, {x: p.count(x) for x in list(p)}, len(p) - 1
#         for i in range(len(s)):
#             check[s[i]] = check.setdefault(s[i], 0) + 1
#             if i >= lp:
#                 if check == dp:
#                     yield i - lp
#                 check[s[i - lp]] = check.setdefault(s[i - lp], 0) - 1
#                 if check.get(s[i - lp]) == 0: del check[s[i - lp]]


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