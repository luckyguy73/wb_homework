from typing import List


class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        # Solution 2 = 28ms
        group, output, combined = {}, [], A.split() + B.split()
        for word in combined:
            group[word] = group.setdefault(word, 0) + 1
        return [k for k, v in group.items() if v == 1]

        # Solution 1 = 32ms
        # A_list, B_list = A.split(), B.split()
        # A_results = [word for word in A_list if word not in B_list if A_list.count(word) == 1]
        # B_results = [word for word in B_list if word not in A_list if B_list.count(word) == 1]
        # return A_results + B_results
