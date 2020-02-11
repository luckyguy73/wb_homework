class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        longest_prefix = ''
        if strs:
            shortest_word = min(strs, key=len)
            for i in range(1, len(shortest_word) + 1):
                if all([x.startswith(shortest_word[:i]) for x in strs]):
                    longest_prefix = shortest_word[:i]
        return longest_prefix
