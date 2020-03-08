import copy


class Solution:
    # @param board, a 9x9 2D array
    # Solve the Sudoku by modifying the input board in-place.
    # Do not return any value.
    def solveSudoku(self, board):
        res = self.dfs(board)
        for n, row in enumerate(res):
            board[n] = ''.join(row)

    def dfs(self, board):
        stack = [board]
        while stack:
            s = stack.pop()
            result = self.fill_board(s)
            if result == 'complete':
                return s
            for r in result:
                stack.append(r)

    def fill_board(self, board):
        digits = set('123456789')
        choice, best = {}, []
        for j in range(9):
            for i in range(9):
                if board[j][i] == '.':
                    square = {board[j // 3 * 3 + y][i // 3 * 3 + x]
                              for y in range(3) for x in range(3)}
                    row = {board[j][x] for x in range(9)}
                    col = {board[y][i] for y in range(9)}
                    rest = digits.difference(square, row, col)
                    if len(rest) == 1:
                        board[j][i] = rest.pop()
                        return self.fill_board(board)
                    elif len(rest) == 0:
                        return ''
                    else:
                        choice[(j, i)] = rest
        if not choice:
            return 'complete'
        y, x = min(choice, key=lambda k: len(choice[k]))
        for n in choice[(y, x)]:
            b = copy.deepcopy(board)
            b[y][x] = n
            best.append(b)
        return best
