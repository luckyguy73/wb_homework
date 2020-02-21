from collections import Counter
from typing import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        punctuation = "!?',;."
        cleansed = ''.join([' ' if t in punctuation else t for t in paragraph])
        cleansed_counts = Counter(cleansed.lower().split()).most_common()
        print(cleansed_counts)
        for word, count in cleansed_counts:
            if word not in banned: return word
