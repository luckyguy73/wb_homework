class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter
        # count = Counter(s)
        # s_sort = sorted(count.items(), key=lambda x: (-x[1], x[0]))
        # results = [k * v for k, v in s_sort]
        # return ''.join(results)

        # count = Counter(s)
        # results = [k * v for k, v in count.most_common()]
        # return ''.join(results)

        return ''.join([k * v for k, v in Counter(s).most_common()])

