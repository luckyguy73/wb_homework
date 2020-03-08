# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        queue = [root]
        for node in queue:
            queue += filter(None, (node.right, node.left))
        return node.val
