from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        dic, neigh = defaultdict(set), defaultdict(set)
        for i, j in prerequisites:
            dic[i].add(j)
            neigh[j].add(i)
        stack, res = [i for i in range(numCourses) if not dic[i]], []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i].remove(node)
                if not dic[i]:
                    stack.append(i)
            dic.pop(node)
        return res if not dic else []
