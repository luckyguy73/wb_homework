# class Solution:
#     def longestWord(self, words: List[str]) -> str:
#         return [w for w in sorted(words, key=lambda x: (-len(x), x)) if all(w[:i] in words for i in range(1, len(w)))][0]
from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        results = {0: ['']}
        for word in sorted(words):
            if word[:-1] in results.get(len(word) - 1, []):
                results.setdefault(len(word), []).append(word)
        return min(results[max(results.keys())])
