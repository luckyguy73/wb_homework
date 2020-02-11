class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        s = bin(N)[2:]
        if s.count('1') < 2: return 0
        ct = m = 0
        for ch in s:
            if ch == '1':
                m = max(ct, m)
                ct = 0
            else:
                ct += 1
        return m + 1
