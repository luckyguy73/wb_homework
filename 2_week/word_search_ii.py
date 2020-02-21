from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(i, j, node, path):
            if board[i][j] in node:
                board[i][j], letter = '', board[i][j]
                node, path = node[letter], path + letter
                if '*' in node: results.add(path)
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < m and 0 <= y < n:
                        dfs(x, y, node, path)
                board[i][j] = letter

        tree, results, m, n = {}, set(), len(board), len(board) and len(board[0])

        for word in words:
            node = tree
            for letter in word + '*': node = node.setdefault(letter, {})

        [dfs(i, j, tree, '') for i in range(m) for j in range(n)]

        return list(results)
