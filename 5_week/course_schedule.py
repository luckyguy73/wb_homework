class Solution:
    def cycle_exists(self, dependencies, index, target):
        if len(dependencies[index]) == 0:
            return False
        elif target in dependencies[index]:
            return True
        else:
            for course in dependencies[index]:
                if self.cycle_exists(dependencies, course, target):
                    return True

            return False

    def canFinish(self, n: int, prerequisites: List[List[int]]) -> bool:
        dependencies = [set() for _ in range(n)]

        for pair in prerequisites:
            dependencies[pair[0]].add(pair[1])

            if self.cycle_exists(dependencies, pair[1], pair[0]):
                return False

        return True
