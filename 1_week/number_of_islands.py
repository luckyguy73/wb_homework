class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid) and len(grid[0])

        def bfs(i, j):
            q, grid[i][j] = [(i, j)], "0"
            for i, j in q:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n and grid[x][y] == "1":
                        grid[x][y] = "0"
                        q.append((x, y))
            return 1

        return sum(bfs(i, j) for i in range(m) for j in range(n) if grid[i][j] == "1")
