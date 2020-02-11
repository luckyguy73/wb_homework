class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n, q = len(board), len(board) and len(board[0]), []

        for r in range(m):
            for c in range(n):
                if (r in (0, m - 1) or c in (0, n - 1)) and board[r][c] == 'O':
                    q.append((r, c))

        while q:
            r, c = q.pop()
            if 0 <= r < m and 0 <= c < n and board[r][c] == 'O':
                board[r][c] = '*'
                q.extend([(r, c + 1), (r, c - 1), (r + 1, c), (r - 1, c)])

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == '*':
                    board[r][c] = 'O'

