class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        matrix = {i + j * 1j: val
                  for i, row in enumerate(matrix)
                  for j, val in enumerate(row)}
        length = {}
        for z in sorted(matrix, key=matrix.get):
            length[z] = 1 + max([length[Z]
                                 for Z in (z + 1, z - 1, z + 1j, z - 1j)
                                 if Z in matrix and matrix[z] > matrix[Z]]
                                or [0])
        return max(length.values(), default=0)
