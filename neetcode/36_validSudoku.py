class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = {}
        rows = {}
        squares = {}

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows.get(r, set()) or 
                    board[r][c] in cols.get(c, set()) or 
                    board[r][c] in squares.get((r // 3, c // 3), set())):
                    return False
                
                if r not in rows:
                    rows[r] = set()
                if c not in cols:
                    cols[c] = set()
                if (r // 3, c // 3) not in squares:
                    squares[(r // 3, c // 3)] = set()

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
