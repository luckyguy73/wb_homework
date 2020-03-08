from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: Node) -> List[int]:
        res = []
        if root is None: return res

        stack = [root]
        while stack:
            curr = stack.pop()
            res.append(curr.val)
            stack.extend(curr.children)

        return res[::-1]
