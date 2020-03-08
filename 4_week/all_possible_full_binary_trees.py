# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def allPossibleFBT(self, N, memos=None):
        """
        :param memos:
        :type N: int
        :rtype: List[TreeNode]
        """
        if memos is None:
            memos = {1: [TreeNode(0)]}
        if N in memos: return memos[N]
        ret = []
        for l in range(1, N - 1, 2):
            for left in self.allPossibleFBT(l):
                for right in self.allPossibleFBT(N - l - 1):
                    root = TreeNode(0)
                    root.left = left
                    root.right = right
                    ret += [root]
        memos[N] = ret
        return ret
