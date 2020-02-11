class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        circle_count, n = 0, len(M)
        visited = [False] * n

        def find_friends(i):
            visited[i] = True
            if not all(visited):
                for j in range(n):
                    if not visited[j] and M[i][j] == 1:
                        find_friends(j)

        for i in range(n):
            if not visited[i]:
                circle_count += 1
                find_friends(i)

        return circle_count
