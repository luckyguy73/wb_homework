class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        matrix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m + 1):
            matrix[i][0] = i
        for j in range(n + 1):
            matrix[0][j] = j

        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if word1[row - 1] == word2[col - 1]:
                    matrix[row][col] = matrix[row - 1][col - 1]
                else:
                    delete = matrix[row - 1][col]
                    insert = matrix[row][col - 1]
                    replace = matrix[row - 1][col - 1]

                    matrix[row][col] = 1 + min(delete, min(insert, replace))

        return matrix[m][n]

